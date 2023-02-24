# Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
# They are also more memory efficient as compared to list comprehensions.

data = [1,2,3,4,5,6]
gen_obj = (x*2 for x in data if x % 2 != 0 )
print(gen_obj)
for x in gen_obj:
    print(x)