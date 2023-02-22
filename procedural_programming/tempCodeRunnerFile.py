def is_palindrome(word):
    startIndex = 0
    endIndex = len(word) - 1
    
    for char in word:
        if word[startIndex] != word[endIndex] :
            return False
        
    return True

word = input(str("Enter a word please: \n"))

print(is_palindrome(word))