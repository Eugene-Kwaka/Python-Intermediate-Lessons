# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
# Write a function to help Bob locate the card.

"""
1. Statement of the Problem 
inputs - The cards listed in decreasing order [10,9,8,7,6,5,4,3,2,1]
query - A card picked by Bob -> 6
output - position of the query in the list of cards [4]
"""
def pick_card(cards, query):
    pass

cards = [10,9,8,7,6,5,4,3,2,1]
query = 6
output = 4

# result = pick_card(cards, query)
# # The result printed will be None as the function does not run anything
# # print(result)

# # The result != output
# result == output

"""
2. Write different testcases that may be applied to the solution of the problem. Read this aloud to the interviewer.

The number query occurs somewhere in the middle of the list cards.
query is the first element in cards. -> 0
query is the last element in cards. -
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.

"""
# The test cases will be represented as dictionaries.
# The input is a dictionary inside a dictionary
test = {
    'input':{
        'cards': [10,9,8,7,6,5,4,3,2,1],
        'query': 6,
    },
    'output': 4
}
# To test the testcase above.
# Whenever we have a dictionary(input), we can use ** to take the keys(cards, query) and their values are used as arguments for the function.
# We equate those values to the desired output
# print the result of the function
# print(pick_card(**test['input']) == test['output'])

""" More Test Cases """
# We store all our test cases in one test list to make it easier to test all
tests = []
# Test case occurs in the middle
tests.append(test)
tests.append({
    'input':{
        'cards': [10,9,8,7,6,5,4,3,2,1],
        'query': 5,
    },
    'output': 5
})

# Query is the first element
tests.append({
    'input':{
        'cards': [10,9,8,7,6,5,4,3,2,1],
        'query': 10,
    },
    'output': 0
})

# Query is the last element
tests.append({
    'input':{
        'cards': [10,9,8,7,6,5,4,3,2,1],
        'query': 1,
    },
    'output': 9
})

# Query only has one element
tests.append({
    'input':{
        'cards': [10],
        'query': 10,
    },
    'output': 0
})

# If the list of cards does not contain the query we are looking for,
# we assume the result(position) of the query will be -1
# Test does not contain the query
tests.append({
    'input':{
        'cards': [10,9,8,7,6,5,4,3,2],
        'query': 1,
    },
    'output': -1
})
# List of cards is empyt
tests.append({
    'input':{
        'cards': [],
        'query': 6,
    },
    'output': -1
})

# Numbers in the card repeat each other
tests.append({
    'input':{
        'cards': [10,9,9,4,4,4,3,3,1],
        'query': 1,
    },
    'output': 9
})

# When we assume the query occurs multiple times in the list,
# then the result will be the position of the first occurrence of the query
tests.append({
    'input':{
        'cards':[10,9,9,4,4,4,3,3,1],
        'query': 1,
    },
    'output': 9
})

"""
3. Write a Brute Force solution. This is not the required solution as it is very straight forward but it works.
I can speak it or write it down for the interviewer.
This type of solution is called a LINEAR SEARCH
"""
# Write a variable position with value of 0.
# Check that the card at index position is equals to query.
# If it does, then that is the result and can be returned by the function
# if not, increment the value of position by 1 and repeat the above steps till we reach the last position.
# if number is not found then return position as -1.


"""
4. Implement the solution and test it using example inputs and fix any bugs.
"""
def pick_cards(cards, query):
    # set the position(index) of the cards as 0
    position = 0
    
    # enter a loop that repeats itself
    while True:
        # check if position of the cards is equal to the card we looking for
        if cards[position] == query:
            # return the answer if TRUE
            return position
        
        # If it doesn't
        # Increment the position to go further the list of cards
        position += 1
        
        # if position is at the end of the list(position equals the length of the cards)
        if position == len(cards):
            return -1
        
print(test)
result = pick_card(test['input']['cards'], test['input']['query'])
result == output
print(result)
# result==output