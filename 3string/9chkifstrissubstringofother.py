#check if string is substring of other 

# Given two strings txt and pat, the task is to find if pat is a substring of txt.
# If yes, return the index of the first occurrence, else return -1.

# Examples : 
# Input: txt = "geeksforgeeks", pat = "eks"
# Output: 2
# Explanation: String "eks" is present at index 2 and 10, so 2 is the smallest index.

# Input: txt = "geeksforgeeks", pat = "xyz"
# Output: -1.
# Explanation: There is no occurrence of "xyz" in "geeksforgeeks"


class Check:
    def chk_if_str_is_substring_of_other(self,str):

        n=len(txt)
        m=len(pat)

        for i in range(n-m+1):#all possible range from where pattern can start 
            j=0

            while j<m and txt[i+j]==pat[j]:
                j+=1

            if j==m:
                return i 

        return -1

txt=input()
pat=input()
ans=Check()
result=ans.chk_if_str_is_substring_of_other(txt,pat)
print(result)