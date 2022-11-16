favorites = ['Pizza', 'Burger', 'Cheese', 'Avocado']

# Counting the number of items in the favorites list.
count = 0 

# Using the while loop 
# While count is less than the number of favorites
while count < len(favorites):
    for item in favorites:
        print("I like this "+  item)
        # I increment the count to match the number of favorites to avoid an infinite loop
        count += 1
        
        
# I count the number of items in favorite list using idx and enumerate the favorites using a for loop
for idx, item in enumerate(favorites):
    # The result will display the index and the items  of the array 
    print(idx, item)

