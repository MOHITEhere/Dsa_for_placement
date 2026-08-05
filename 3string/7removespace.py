# remove space from a given substring 

# Given a string s, remove all spaces from the string
# and return it. 

# Examples:

# Input:  s = "g  eeks   for ge  eeks  "
# Output: geeksforgeeks
# Explanation: All the spaces have been removed.

# Input:  s = "   abc d "
# Output: abcd
# Explanation: All the spaces including the leading ones have
# been removed.
def substring(s):
    n=len(s)
    result=''
    
    for ch in s:
        if ch!=" ":
            result+=ch
    return result

s='   abc d '
print(substring(s))
