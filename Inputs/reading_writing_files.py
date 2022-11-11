# Close -> Closes the file

# Read ->  Reads the contents of the file. I can assign the result to a variable

# readline -> Reads just one line of a text.

# truncate -> Empties the file. Removes all contents

# write('stuff') -> Writes stuff/content to the file

# seek(0) -> Moves the read/write location to the beginning of the file. 

from sys import argv

script, file_name = argv

# Open a file
text = open(file_name)
print(f"Here's your file {file_name}: ")

# Read the contents of the file name 
print(text.read())

print("Type your file name again: ")
file_again = input("> ")

# Open the file you input above
text_again = open(file_again)

# Read the contents of the file
print(text_again.read())




####################### WRITING A FILE ##############################
from sys import argv
script, file_name = argv

file_name = open(file_name, 'r+')
print("Opening the file....")
# prompt inputs that I add to my file
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
# Write the above inputs into our file
file_name.write(line1 + "\n" + line2 + "\n" + line3)

# print for the contents to be displayed
print(file_name.read())

# # close the file to save the contents
# file_name.close()

