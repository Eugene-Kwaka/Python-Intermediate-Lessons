# THE SYNTAX FOR SLICE FUNCTION
"""str[start:stop:step]
"""

trial = "revere"
new_trial = trial[::-1]
"""
The -1 tells python to slice from the farthest right going to the left by 1 index at a time, hence the reversal.
This is in contrary to the normal start from the left -> right way.
"""
print(new_trial)

# USING RECURSION
def str_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str_reverse(str[1:]) + str[0]
    """
    The string is traversed from the front skipping the 1st character in every loop appending it to the remaining string.
    """
    
str = "reversal"
print(str_reverse(str))