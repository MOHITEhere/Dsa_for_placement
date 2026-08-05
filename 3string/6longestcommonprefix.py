#longest common prefix 

# Given an array of strings arr[], return the longest common prefix among each 
# and every strings present in the array. If there’s no prefix common in all the strings, return “”.

# Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
# Output: “gee”
# Explanation: “gee” is the longest common prefix in all the given strings: “geeksforgeeks”, “geeks”, “geeks” and “geezer”.

# Input: arr[] = [“apple”, “ape”, “april”]
# Output : “ap”
# Explanation: “ap” is the longest common prefix in all the given strings: “apple”, “ape” and “april”.

# Input: arr[] = [“hello”, “world”]
# Output: “”
# Explanation: There’s no common prefix in the given strings.

class LCP:
    def longest_common_prefix(self,n,str):

        result=""
        str.sort()
        min=len(str[0])

        for i in range(min):
            if str[0][i]==str[-1][i]:
                result+=str[0][i]

        return result


n=int(input())
str=input().split()
ans=LCP()
result=ans.longest_common_prefix(str)
print(result)