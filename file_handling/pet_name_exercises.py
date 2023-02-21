# Imagine you are trying to come up with a name for your new dog. 
# You're really unsure of what you'd like to call the dog, so you decide to use your Python skills to help you decide.

import random

with open(r"C:\Users\Eugene Kwaka\Desktop\PYTHON-INTERMEDIATE-TUTORIALS\file_handling\pet_names.txt", "r") as file:
    file_content = file.read()
    # To print the file contents in a list, I use '\n'.
    # The split() function splits a string into a list
    pet_names = file_content.split()
    print(pet_names)
# To choose a pet name randomly, I will use the random.choice() function
my_pet = random.choice(pet_names)
print(my_pet)
