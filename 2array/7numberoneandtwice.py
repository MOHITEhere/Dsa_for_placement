#number that come's once and other's twice 

# Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
# Output: 2 
# Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

# Input: arr[] = [2, 2, 5, 5, 20, 30, 30]
# Output: 20
# Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.

class Count:
    resut=0

    def single(arr):
        for num in arr:
            result^=num

        return result

arr=list(map(int,input().split()))
print(Count(arr))


