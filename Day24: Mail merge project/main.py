PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()
    # print(content)
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)
    for name in names:
        stripped_name = name.strip()
        letter = content.replace(PLACEHOLDER, stripped_name)
        print(letter)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(letter)

