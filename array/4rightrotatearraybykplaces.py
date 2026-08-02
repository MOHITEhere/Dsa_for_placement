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

