# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     return squared_numbers

# numbers = [2,4,6,8]
# print(get_squared_numbers(numbers))


# Search for duplicate numbers
numbers = [3,6,2,4,3,6,8,9]
duplicate = None
# for an index in the total indices of the list
for i in range(len(numbers)):
    # for the index j in range of of the index i+1 and indices of the list
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break
        
print(f"Duplicate number is: ", duplicate)

for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(f"The positional index of the duplicate number is: ", i)