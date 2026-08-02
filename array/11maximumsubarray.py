# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

'''USE KANDANE's ALgorithm'''

class Maximum_subarray:

    def maximumsubarray(self,arr):
        all_positive=all(i>0 for i in arr)
        all_negative=all(i<0 for i in arr)

        if all_positive:
            return sum(arr)
        if all_negative:
            return max(arr)
        
        max_sum=0
        for i in range(len(arr)):
            sum=0
            for j in range(i,len(arr)):
                sum+=arr[j]
                max_sum=max(sum,max_sum)

        return max_sum

    #OPTIMIZED
    def maximumsubarray_kandane(self,arr):
        current_sum=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
            current_sum=max(current_sum,current_sum+arr[i])
            max_sum=max(max_sum,current_sum)

        return max_sum

arr=list(map(int,input().split()))
ans=Maximum_subarray()
result=ans.maximumsubarray(arr)
