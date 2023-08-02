import csv
FILENAME = "characters.csv"

"""Using the standard file reader and split method."""
# with open(FILENAME, "r") as file:
#     for character in file:
#         name, actor, role, description, seasons, status = character.split(",")
#         print(name)

"""Using the standard CSV Reader."""
# with open(FILENAME) as file:
#     for character in csv.reader(file):
#         character_name = character[0]
#         print(character_name)

"""Using the DictReader within the CSV module."""
# with open(FILENAME) as file:
#     dict_reader = csv.DictReader(file)

#     for character in dict_reader:
#         print(character["name"])
