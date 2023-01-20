with open('testing.txt', 'r') as file:
    # READ() returns the whole contents of the file as a string.
    # I can specify how many characters to be displayed from the file
     the_file = file.read(5)
     print(the_file)
     
######  READLINE(n) returns the specified number of characters on a line  ##########
with open('new_file.txt', 'r') as file:
    # Will display the first 10 characters from the first line
    the_file = file.readline(10)
    print(the_file)
    
    
##### READLINES() returns the entire content of the file and returns an unordered list #########
with open('new_file.txt', 'r') as file:
    the_file = file.readlines()
    for lines in the_file:
        print(lines)