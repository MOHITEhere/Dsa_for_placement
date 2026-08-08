# take example of n=5 and output 8 with explanation in single message
# Input:
# n = 5

# Output:
# 8

# Explanation:
# You can climb either 1 or 2 steps at a time.

# The 8 distinct ways to reach the 5th stair are:

# 1. 1 + 1 + 1 + 1 + 1
# 2. 1 + 1 + 1 + 2
# 3. 1 + 1 + 2 + 1
# 4. 1 + 2 + 1 + 1
# 5. 2 + 1 + 1 + 1
# 6. 1 + 2 + 2
# 7. 2 + 1 + 2
# 8. 2 + 2 + 1

#steps:1,2

class Climbing:
    def climbing_stairs(self,n):
        if n<=0:
            return 0
        if n<=1:
            return 1 
        if n<=2:
            return 2 
        
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]

n=int(input())
ans=Climbing()
result=ans.climbing_stairs(n)
print(result)