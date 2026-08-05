#right rotate an array by k places 


class RotateByKPlaces:

    def left_rotate(self,arr,k):
        n=len(arr)
        k=k%n

        if n==0:
            return arr

        arr[:]=arr[k:]+arr[:k]
        return arr

    def right_rotate(self,arr,k):
        n=len(arr)
        k=k%n

        if n==0:
            return arr

        arr[:]=arr[-k:]+arr[:-k]
        return arr


arr=list(map(int,input().split()))
k=int(input())

ans=RotateByKPlaces()
result1=ans.left_rotate(arr,k)
result2=ans.right_rotate(arr,k)


#optimized 


def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    return arr

def right_rotate(arr,k):
    n=len(arr)
    k=k%n

    reverse(arr,0,n-1) #reverse whole array
    reverse(arr,0,k-1) #reverse 1st k terms
    reverse(arr,k,n-1) #reverse remaining 

    return arr

def left_rotate(arr,k):
    n=len(arr)
    k=k%n

    reverse(arr,0,k-1)#first k rotate
    reverse(arr,k,n-1)#remaining k rotate
    reverse(arr,0,n-1) #rotate all

    return arr 

arr=list(map(int,input().split()))
print(right_rotate(arr))
    





