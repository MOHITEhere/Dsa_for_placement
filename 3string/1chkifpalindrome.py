#CHECK IF STRING IS PALINDROME

# Input: s = "abba"
# Output: true
# Explanation: s is a palindrome

# Input: s = "abc" 
# Output: false
# Explanation: s is not 
# a palindrome
class Palindrome:
    def check_palidrome(self,str):
        low=0
        high=len(str)-1

        while low<high:
            if str[low]!=str[high]:
                return "Not Palindrome"
            else:
                low+=1
                high-=1

        return "palindrome"


    def check_palindrome(self,str):
        return str==str[::-1]


str=input()
ans=Palindrome()
result=ans.check_palidrome(str)
print(result)