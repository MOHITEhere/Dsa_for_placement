# Buy and Sell Stock (Multiple Transactions)

# You are given an array prices[] where:

# prices[i] represents the stock price on day i
# 🎯 Goal

# 👉 Maximize profit by:

# Buying and selling the stock multiple times
# You must sell before buying again
# 🧠 Greedy Idea

# 👉 Capture every increasing price difference

# If today’s price > yesterday’s → take profit
# prices = [7, 1, 5, 3, 6, 4]
# 7
# Day 1 to 2: Price goes from 7 to 1 (Decrease - Skip)
# Day 2 to 3: Price goes from 1 to 5 (Increase - Buy at 1, Sell at 5) - Profit = 5 - 1 = 4
# Day 3 to 4: Price goes from 5 to 3 (Decrease - Skip)
# Day 4 to 5: Price goes from 3 to 6 (Increase - Buy at 3, Sell at 6) - Profit = 6 - 3 = 3
# Day 5 to 6: Price goes from 6 to 4 (Decrease - Skip)
# Total Profit: 4 + 3 = 7



class Buyandsellstoks:
    def buy_and_sell_stocks(self,prices):
        n=len(prices)
        total=0
        for i in range(n-1):
            if prices[i]<prices[i+1]:
                total+=prices[i+1]-prices[i]

        return total

prices=list(map(int,input().split()))
ans=Buyandsellstoks()
result=ans.buy_and_sell_stocks(prices)
print(result)