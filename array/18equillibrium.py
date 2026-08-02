# Input: arr[] = [1, 2, 0, 3]
# Output: 2
# Explanation: The sum on the left of index 2 is 1 + 2 = 3 and sum on the right of index 2 is 3.

# Input: arr[] = [1, 1, 1, 1]
# Output: -1 
# Explanation: There is no equilibrium index in the array.

# Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
# Output: 3
# Explanation: The sum on the left of index 3 is -7 + 1 + 5 = -1 and sum on the right of index 3 is -4 + 3 + 0 = -1.

def equillibriumpooint(arr):
    total_sum=sum(arr)
    left_sum=0

    for i in range(len(arr)):
        right_sum=total_sum-left_sum-arr[i]
        #right sum kaise milega total mein se left aur current nikalke 

        if left_sum==right_sum:
            return i+1 #note yaha pe i+1
        
        
        left_sum+=arr[i]

    return -1 

arr= [1, 2, 0, 3]
print(equillibriumpooint(arr))
