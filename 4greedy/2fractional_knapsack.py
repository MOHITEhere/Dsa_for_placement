# Problem: Fractional Knapsack (Greedy)

# You are given n items, where each item has:

# a value
# a weight

# You are also given a knapsack with capacity W
# 🎯 Goal
# 👉 Maximize the total value in the knapsack such that:
# Total weight ≤ W
# ⚡ Special Rule
# 👉 You are allowed to take fractions of items

# You can take a full item
# OR a part of an item
# 🧾 Example

# Input:
# values  = [60, 100, 120]
# weights = [10, 20, 30]
# W = 50

class Knapsack:
    def fractional_knapsack(self, values, weights, w):
        n = len(weights)  
        items = []
        for i in range(n):
            ratio = values[i] / weights[i]
            items.append((ratio, values[i], weights[i]))

        items.sort(key=lambda x: x[0], reverse=True)

        remaining = w
        total = 0.0

        for i in range(n):
            ratio, v, wt = items[i]  

            if wt <= remaining:
                remaining -= wt
                total += v
            else:
                total += remaining * ratio
                remaining = 0
                break 

        return total


values = list(map(int, input().split()))
weights = list(map(int, input().split()))
w = int(input())

ans = Knapsack()
result = ans.fractional_knapsack(values, weights, w)
print(result)