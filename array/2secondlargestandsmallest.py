class Largestsmallest:
    def slass(self,arr):
        a=[]
        for i in arr:
            if i not in a:
                a.append(i)


        a.sort()

        return [a[1],a[-2]]



arr=list(map(int,input().split()))
ans=Largestsmallest()
result=ans.slass(arr)
print(result)

#tc and sc=O(n^2),O(n)

'optimised'

def opti_slass(arr):
    smallest=second_smallest=float('inf')
    largest=second_largest=float('-inf')

    if len(arr)<2:
        return [-1,-1]

    for num in arr:
        if num<smallest:
            second_smallest=smallest
            smallest=num

        elif num<second_smallest and num!=smallest:
            second_smallest=num

        if num>largest:
            second_largest=largest
            largest=num

        elif num>second_largest and num!=largest:
            second_largest=num 

        #if number in arr are unique and same 

        if second_largest==float('-inf') or second_smallest==float('inf'):
            return[-1,-1]

        return [second_smallest,second_largest]


arr=list(map(int,input().split()))
result=opti_slass(arr)
print(result)