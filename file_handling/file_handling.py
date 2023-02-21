file = open(r"C:\Users\Eugene Kwaka\Desktop\PYTHON-INTERMEDIATE-TUTORIALS\file_handling\testing.txt", mode='r') #The mode for the file is read only
# readline() displays the first line of the document I opened
data =  file.readline()
print(data)
file.close()

### A better recommended way is to use "with"
with open(r"C:\Users\Eugene Kwaka\Desktop\PYTHON-INTERMEDIATE-TUTORIALS\file_handling\testing.txt", 'r') as file:
    my_file = file.readline()
    print(my_file)