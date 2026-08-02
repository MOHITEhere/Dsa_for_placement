#largest and smallest element in array 


class Largestsmallest:
    def laseia(self,arr):

        if not arr:
            return [-1,-1]
        
        largest=float('-inf')
        smallest=float('inf')

        for i in arr:
            if i>largest:
                largest=i
            if i<smallest:
                smallest=i


        return [smallest,largest]


arr=list(map(int,input().split()))
ans=Largestsmallest()
result=ans.laseia(arr)
print(result)