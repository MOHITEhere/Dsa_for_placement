# Problem: Indian Coins (Greedy Approach)
# You are given an amount N (in rupees).
# You have an infinite supply of Indian currency denominations:

# [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# 🎯 Goal
# 👉 Find the minimum number of coins/notes required to make the given amount N.
# ⚡ Constraint
# You can use any denomination multiple times
# You must minimize the total number of coins/notes

# 🧾 Example
# Input:
# N = 289
# 🔍 Explanation
# Using greedy (largest first):
# 200 → remaining 89  
# 50  → remaining 39  
# 20  → remaining 19  
# 10  → remaining 9  
# 5   → remaining 4  
# 2   → remaining 2  
# 2   → remaining 0  

# ✅ Output:
# Minimum coins = 7
# Coins used = [200, 50, 20, 10, 5, 2, 2]


class Coin:
    def indian_coins(self,amount,coins):
        coins.sort(reverse=True)

        count=0

        for coin in coins:
            if amount>=coin:
                count+=amount//coin
                amount%=coin

            if amount==0:
                break 


        return count



amount=int(input())
coins=list(map(int,input().split()))
ans=Coin()
result=ans.indian_coins(amount,coins)
print(result)
