print("how tall are you? ", end='')
height = input()
print("How old are you anyway? ", end='')
age = input()
print("What is your weight? ", end='')
weight = input()

print(f"So you are {age} yrs old, weigh {weight} and {height} in height")


######################## PARAMETERS, UNPACKING, VARIABLES ###############################
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# To run this, in the terminal I will write: "python main.py first, second, third".
# The variables will be assigned those values as arguments that are written in the terminal and will be printed in the output