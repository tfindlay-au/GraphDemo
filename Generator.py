import names
import random

# Generate unique list
name_data = set()
while len(name_data) < 1000000:
    name_data.add(names.get_full_name().replace(" ", "_"))

# Output the list /w hair_color
f = open("nodes.csv", "a")
f.write("_key, hair_color\n")
for n in name_data:
    hair_color = ['Black', "Blue", "Red", "White", "Brown", "Grey"]
    f.write("{0}, {1}\n".format(n, random.choice(hair_color)))
f.close()

# Whilst we are here, make edges
f = open("edges.csv", "a")
f.write("_from,_to\n")
last_person = ""
for n in name_data:
    f.write("people/{0},people/{1}\n".format(last_person, n))
    last_person = n
f.close()
