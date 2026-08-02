class Check:

    def check_sorted(self,arr):

        if len(arr)<=1:
            return "Sorted"

        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                return "Unsorted"

            return "sorted"



arr=list(map(int,input().split()))
ans=Check()
result=ans.check_sorted(arr)
print(result)