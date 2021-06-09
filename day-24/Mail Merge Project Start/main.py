# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


f = open(
    "100DaysOfCode/100daysOfCode/day-24/Mail Merge Project Start/Input/Names/invited_names.txt",
    "r",
)

l = open(
    "100DaysOfCode/100daysOfCode/day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt",
    "r",
)

invited_names = f.readlines()
starting_letter = l.readlines()

print(invited_names)
print(len(invited_names))

print(starting_letter)

for name in invited_names:

    # new_letter = starting_letter.replace(f"[name]", "{name}")
    pass
