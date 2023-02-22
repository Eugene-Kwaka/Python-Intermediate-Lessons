def is_palindrome(word):
    startIndex = 0
    endIndex = len(word) - 1
    
    for char in word:
        if word[startIndex] != word[endIndex] :
            return False
        
    return True

word = input(str("Enter a word please: \n"))

print(is_palindrome(word))

#### A MORE EFFECIENT ANSWER IS:

def is_palindrome(s):
    """
    Returns True if the given string s is a palindrome, and False otherwise.
    """
    # Convert the string to lowercase to make the comparison case-insensitive.
    s = s.lower()

    # Remove all non-alphanumeric characters from the string.
    s = ''.join(c for c in s if c.isalnum())

    # Compare the string to its reverse. If they are equal, it's a palindrome.
    return s == s[::-1]

s = input(str("write a word/sentence: \n "))

print(is_palindrome(s))