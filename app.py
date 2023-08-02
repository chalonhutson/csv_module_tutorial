FILENAME = "characters.csv"

with open(FILENAME, "r") as file:
    for character in file:
        name, actor, role, description, seasons, status = character.split(",")
        print(name)

    # print([len(character.rstrip().split(",")) for character in file])
