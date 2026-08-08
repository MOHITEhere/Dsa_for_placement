#  Problem Statement

# Given an array of integers nums and an integer target_sum,
# determine if there exists a subset of the array whose sum is equal to target_sum.

# Example
# Input:

# nums = [4, 2, 7, 1, 3]  
# target_sum = 7

# Output:
# True

# Explanation (short):
# Subset [4, 2, 1] gives sum = 7
# Also [7] itself is valid.

class Targetsum:
    def target_sum_subset(self,nums,target):
        n=len(nums)

        dp=[[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=True 

        for i in range(1,n+1):
            for j in range(1,target+1):

                if nums[i-1]<=j:
                    dp[i][j]=(
                        dp[i-1][j]
                        or 
                        dp[i-1][j-nums[i-1]]
                    )
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][target]

nums=list(map(int,input().split()))
target_sum=int(input())
ans=Targetsum()
result=ans.target_sum_subset(nums,target_sum)
print(result)