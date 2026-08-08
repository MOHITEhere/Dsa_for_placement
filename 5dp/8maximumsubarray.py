class Maximum:
    def maximum_subarray(self,arr):
        n=len(arr)
        dp=[0]*(n+1)

        dp[0]=arr[0]

        for i in range(1,n):
            dp[i]=max(arr[i],dp[i-1]+arr[i])

        return max(dp)

arr=list(map(int,input().split()))
ans=Maximum()
result=ans.maximum_subarray(arr)
print(result)


class Maximum2:
    def max_subarray(self,arr):
        n=len(arr)
        if n==0:
            return 0
        
        curr=arr[0]
        best=arr[0]

        for i in range(1,n):

            curr=max(arr[i],curr+arr[i])
            best=max(curr,best)

        return best

arr=list(map(int,input().split()))
ans=Maximum()
result=ans.maximum_subarray(arr)
print(result)