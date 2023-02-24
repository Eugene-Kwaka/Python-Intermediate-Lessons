# LET ME LOOK AT HOW TO CHANGE A FUNCTION FROM NORMAL TO PURE FUNCTION

# NORMAL FUNCTION
my_list = [1,2,3]

# def add_to_list(item):
#     return my_list.append(item)

# add_to_list(4)

# print(my_list)

## CHANGING TO PURE FUNCTION
"""Function takes in a list(my_list) and the new item to be added, as its arguments """
def add_to_list(list, item):
    """the nl variable copies the elements from my_list """
    nl = list.copy(my_list)
    """Then appends the new item to be added"""
    nl.append(item)
    return nl

new_list = add_to_list(list, 4)

print(my_list)
print(new_list)