# I want to create a new list with the coffees that start with  c
menu = ["espresso", "mocha", "latte", "cappucino", "cortada", "americano"]

# print(new_list)
def locate_coffee(coffee):
    if coffee[0] == "c":
        return coffee

new_menu = map(locate_coffee, menu) 
"""
-> map function takes all the elements in a list and applies the function passed as its argument, returning all values.
"""
print(new_menu)
for x in new_menu:
    print(x)

new_menu = filter(locate_coffee, menu)
"""
-> filter function takes all the elements and applies the function passed as its arguments. It creates a new list containing the output values that are True.
"""
print(new_menu)
for x in new_menu:
    print(x)