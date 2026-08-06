# Problem: Circular Gas Station

# You are given two arrays:

# gas[i] → amount of gas available at station i
# cost[i] → gas required to travel from station i to (i+1)

# 👉 The stations are arranged in a circular manner.

# 🎯 Goal

# 👉 Find the starting gas station index from where you can:

# travel the entire circle once
# without running out of gas

# 👉 If not possible, return -1

# 🧾 Example

# Input:

# gas  = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# 🔍 Explanation

# Try starting from index 3:

# Start at 3 → gas = 4

# 4 - 1 = 3  
# 3 + 5 = 8 → 8 - 2 = 6  
# 6 + 1 = 7 → 7 - 3 = 4  
# 4 + 2 = 6 → 6 - 4 = 2  
# 2 + 3 = 5 → 5 - 5 = 0  

# 👉 Completed full circle ✅

# ✅ Output:
# 3


class Gas:
    def gas_station(self,gas,cost):
        if sum(gas)<sum(cost):
            return -1 

        start=0
        tank=0

        for i in range(len(gas)):
            tank+=gas[i]-cost[i]

        if tank<0:
            start=i+1
            tank=0

        return start


gas=list(map(int,input().split()))
cost=list(map(int,input().split()))
ans=Gas()
result=ans.gas_station(gas,cost)
print(result)