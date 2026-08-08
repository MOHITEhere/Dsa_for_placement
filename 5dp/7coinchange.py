#Problem Statement — Coin Change (Number of Combinations)

# Given an array of coin denominations coins[] and an integer amount
# determine the total number of unique combinations that make up the given amount.

# You have infinite supply of each coin
# Order of coins does not matter (combinations, not permutations)
# 🔹 Example

# Input:

# coins = [1, 2, 5]
# amount = 5

# Output:

# 4
# 🔹 Explanation (short)

# Possible combinations are:

# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 2 + 2
# 5'

#same like climbing stairs but steps are 1,2and5
class Change:
    def coin_change(self,coins,amount):
        n=len(coins)

        dp=([0]*(amount+1) for _ in range(n+1))

        for i in range(n):
            dp[i][0]=1

        for i in range(1,n+1):
            for j in range(amount+1):

                if coins[i-1]<=j:
                    dp[i][j]=(
                        dp[i-1][j]
                        +
                        dp[i][j-coins[i-1]]
                    )

                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][amount]
        

coins=list(map(int,input().split()))
amount=int(input())
ans=Change()
result=ans.coin_change(coins,amount)
print(result)
