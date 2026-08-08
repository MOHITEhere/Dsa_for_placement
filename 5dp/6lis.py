# #longest increasing sequence 
# Problem Statement — Longest Increasing Subsequence (LIS)

# Given an array of integers arr, find the length of the longest subsequence such that:

# Elements are in increasing order
# Subsequence does not need to be contiguous
# Each next element must be strictly greater than the previous one
# 🔹 Example

# Input:
# arr = [50, 3, 10, 7, 40, 80]
# Valid Increasing Subsequences:
# 50, 80
# 3, 10, 40, 80
# 3, 7, 40, 80   ← longest
# 10, 40, 80
# 7, 40, 80
# 40, 80

# Output:
# 4


class Subsequence:
    def longest_increasing_subsequence(self,arr):
        sorted_arr=sorted(arr)

        n=len(arr)
        m=len(sorted_arr)

        dp=([0]*(m+1) for _ in range(n+1))

        for i in range(1,n+1):
            for j in range(1,m+1):
                if arr[i-1]==sorted_arr[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])

        return dp[n][m]
    
        


arr=list(map(int,input().split()))
ans=Subsequence()
result=ans.longest_increasing_subsequence(arr)
print(result)