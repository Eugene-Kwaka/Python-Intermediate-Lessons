with open("new_file.txt", 'w') as file:
    # file.write("I just created this")
    # To write multiple lines I use writelines()
    file.writelines(['This is dope', '\nHandling files with Python', '\nFinally know how to'])

# To add new text to new_file.txt without rewriting everything I use mode 'a' to append
with open('new_file.txt', 'a') as file:
    file.writelines(["\nAdded a new line", "\nIsn't this cool"])