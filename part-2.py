# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    
    if array[0] == query:
        return True
    
    return search(array[1:], query)


# is_palindrome

# def is_palindrome(text):
#     if text == reverse(text):
#         return True
#     return False
    
# def reverse(text):
#     if len(text) == 1:
#         return text
#     reverse(text[1:]) + text[0]
    
    
def is_palindrome(text):
    if len(text) < 2:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1: -1])


# digit_match

def digit_match(num1, num2):

    if num1<10 or num2<10:
        if num1 % 10 == num2 % 10:
            return 1
        else:
            return 0
            
    if num1 % 10 == num2 % 10:
        count = 1
    else:
        count = 0
        
  
    return count + digit_match(num1//10,  num2//10)

        
