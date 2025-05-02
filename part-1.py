# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0 or not isinstance(n,int):
        raise ValueError("n must be a non-negative number")
    if n < 2:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    # first word always put in the last
    
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]



# bunny

def bunny(count):
    if count ==0:
        return 0
    return 2+bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
        
    if len(parens) == 1:
        return False
    
    if parens[0] == "(" and parens[-1] ==")":
        return is_nested_parens(parens[1:-1])

