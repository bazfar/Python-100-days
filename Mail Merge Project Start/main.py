PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letters_file:
    letters_content = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters_content.replace(PLACEHOLDER, f"{stripped_name}")
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output_file:
            output_file.write(new_letter)
