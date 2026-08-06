# Input:

# a = [4, 1, 8, 7]
# b = [2, 3, 6, 5]
# 🔍 Explanation
# Step 1: Sort both arrays
# a = [1, 4, 7, 8]
# b = [2, 3, 5, 6]
# Step 2: Pair corresponding elements
# |1-2| = 1  
# |4-3| = 1  
# |7-5| = 2  
# |8-6| = 2  
# ✅ Output:
# Total = 6
# 🧠 Key Insight

# 👉 To minimize difference:

# Pair smallest with smallest, largest with largest

# ⏱️ Complexity
# Sorting: O(n log n)
# Pairing: O(n)
# 🎯 Interview Insight

# 👉 This is a classic greedy problem

# Sorting ensures minimum difference pairing
# Any other pairing increases total difference

# If you want next:

# I can show proof why greedy works (important concept)
# or 
# give wrong pairing example (to build intuition)

class Difference:
    def min_abs_differnce(self,a,b):
        a.sort()
        b.sort()

        n=len(a)
        total=0

        for i in range(n):
            ans=abs(a[i]-b[i])
            total+=ans

        return total

    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=Difference()
result=ans.min_abs_differnce(a,b)
print(result)