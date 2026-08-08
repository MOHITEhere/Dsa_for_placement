# Input:
# Weights = [1, 2, 3]
# Values  = [10, 15, 40]
# Capacity = 6

# Output:
# 65

# Explanation:
# You can either take an item completely or not take it at all (0/1 Knapsack).

# Possible selections:
# 1. Item 1 (Weight = 1, Value = 10)
# 2. Item 2 (Weight = 2, Value = 15)
# 3. Item 3 (Weight = 3, Value = 40)

# Since the total weight is:
# 1 + 2 + 3 = 6 (within the capacity)

# Total value:
# 10 + 15 + 40 = 65

# Hence, the maximum value that can be obtained is 65.
class Knapsack:
    def knapsack_01(self,weights,values,w):
        n=len(weights)

        dp=[0]*((w+1) for _ in range(n+1))

        for i in range(1,n+1):

            for j in range(w+1):

                if weights[i-1]<=j:
                    dp[i][j]=max(
                        values[i-1]+dp[i-1][j-weights[i-1]],
                        dp[i-1][j]
                    )
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][w]
 


weights = [1, 2, 3]
values  = [10, 15, 40]
capacity = 6
ans=Knapsack()
result=ans.knapsack_01(weights,values,capacity)
print(result)