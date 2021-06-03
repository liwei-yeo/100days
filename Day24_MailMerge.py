# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day24_Input/Letters/starting_letter.txt") as file:
    template = file.read()

with open("./Day24_Input/Names/invited_names.txt") as file:
    # readlines returns as list of lines
    namelist = file.readlines()

for name in namelist:
    name = name.strip("\n")
    content = template.replace("[name]", name)
    with open(f"./Day24_Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(content)

