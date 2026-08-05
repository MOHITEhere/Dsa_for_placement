# #check whether the number is palindrome or not
# Input: n = 12321
# Output: True
# Explanation: 12321 is a palindrome number because it reads same  forward and backward.

# Input: n = -121
# Output: True
# Explanation:  We number is palindrome, we mainly ignore sign.

# Input: n = 1234
# Output:  False
# Explanation: 1234 is not a palindrome number because it does not read the same forward and backward.

class Check:
    def check_palindrome(nself,num):
        if num==num[::-1]:
            return "Palindrome"
        else:
            return "Not palindrome"


num=int(input())
ans=Check()
result=ans.check_palindrome(num)
print(result)

