# Longest Common Subsequence (LCS) — Problem

# Given two strings s1 and s2, find the length of the longest subsequence 
# that appears in both strings (not necessarily contiguous).

# Example

# Input:

# s1 = "abcde"
# s2 = "ace"

# Output:

# 3

# Explanation (short):
# Common subsequence = "ace" → length = 3

class Subsequence:
    def longest_common_subsequence(self,str1,str2):
        n=len(str1)
        m=len(str2)

        dp=([0]*(m+1) for _ in range(n+1))

        for i in range(1,n+1):
            for j in range(1,m+1):

                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[n][m]
    
   


str1=input()
str2=input()
ans=Subsequence()
result=ans.longest_common_subsequence(str1,str2)
print(result)