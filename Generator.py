##############################################################
# Purpose: Generate random names and pick a random hair color
#
# Notes: Example only.
#
import names
import random

# Generate unique list
name_data = set()
while len(name_data) < 1000000:
    name_data.add(names.get_full_name().replace(" ", "_"))

# Output the list /w hair_color
nodeFile = open("nodes.csv", "a")
nodeFile.write("_key, hair_color\n")
for n in name_data:
    hair_color = ['Black', "Blue", "Red", "White", "Brown", "Grey"]
    nodeFile.write("{0}, {1}\n".format(n, random.choice(hair_color)))
nodeFile.close()

# Whilst we are here, make edges
edgeFile = open("edges.csv", "a")
edgeFile.write("_from,_to\n")
last_person = None
for n in name_data:
    if last_person is None:
        last_person = n
    else:
        edgeFile.write("people/{0},people/{1}\n".format(last_person, n))
        last_person = n
edgeFile.close()
