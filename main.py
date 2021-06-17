PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt', mode='r') as file:
    names = file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    content = letter_file.read()
    for name in names:
        stripped= name.strip()
        new_content = content.replace(PLACEHOLDER, stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt" , mode='w') as final:
            x = final.write(new_content)

