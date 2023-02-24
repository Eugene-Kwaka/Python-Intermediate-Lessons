data = [1,2,3,4]
data = [x+2 for x in data]
print(data)

new_data = [2,4,6,8,10,12]
updated = [x for x in data if x % 4 ==0]
print(updated)

list = [x*2 for x in range(100) if x % 5 == 0]
print(list)