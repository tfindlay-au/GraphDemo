##############################################################
# Purpose: Demonstrate inserting a single record at a time into an ArangoDB
#
# Notes: This is simple for demonstration purposes, but very slow. Dont use this code.
#
from pyArango import connection, theExceptions
import names
import random

# Create a connection to the DB
conn = connection.Connection(arangoURL="http://10.1.20.6:8529", username="root", password="openSesame")

# Create database if not exists
if not conn.hasDatabase("DataEngineeringMelbourne"):
    conn.createDatabase(name="DataEngineeringMelbourne")
db = conn["DataEngineeringMelbourne"]

# Create collection if not exists
if not db.hasCollection("people"):
    db.createCollection(name="people")
collection = db["people"]

# Iterate to generate data
for i in xrange(1000000):
    hair_color = ['Black', "Blue", "Red", "White", "Brown", "Grey"]

    # _key must be unique, trap exceptions if duplicates are created
    try:
        doc = collection.createDocument()
        doc["_key"] = names.get_full_name().replace(" ", "_")
        doc["hair_color"] = random.choice(hair_color)
        doc.save()
    except theExceptions.CreationError:
        print("Skipping duplicate: {}", doc["_key"])
