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
    def circular_gas_station(self,gas,cost):
        if sum(cost)>sum(gas):
            return -1 
            
        ans=0
        start=0
        
        for i in range(len(gas)):
            ans+=gas[i]-cost[i]
            if ans<0:
               start=i+1
               ans=0
                
        return start
                
            
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
ans=Gas()
result=ans.circular_gas_station(gas,cost)
print(result)
