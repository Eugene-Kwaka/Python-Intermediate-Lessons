# Dictionary comprehensions take the following syntax:
"""
dict = {key:value for key, value in <sequence> if <condition>}
"""

## Using range() as input
using_range = {x:x*2 for x in range(11)}
print(f"Using range: ", using_range)

## Using list as input
list = [1,2,3,4,5]
new_list = {x:x+2 for x in list if x%2 != 0}
print(new_list)

## Using two lists as input
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]
calendar = {number:months for number,months in zip(number, months)}
print(calendar)