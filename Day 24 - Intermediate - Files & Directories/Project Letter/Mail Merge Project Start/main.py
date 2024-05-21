with open("Day 24 - Intermediate - Files & Directories/Project Letter/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Day 24 - Intermediate - Files & Directories/Project Letter/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    for name in names:
        name = name.strip()
        send_letter = letter.replace("[name]", name)
        

        with open(f"Day 24 - Intermediate - Files & Directories/Project Letter/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}.txt", mode="w") as file:
            file.write(send_letter)