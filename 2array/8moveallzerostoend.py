# put: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.

class Move:

    def movezero(self,arr):
        count_zero=arr.count(0)

        for _ in range(count_zero):
            arr.remove(0)

        for _ in range(count_zero):
            arr.append(0)

        return arr

arr=list(map(int,input().split()))
ans=Move()
result=ans.movezero(arr)
print(result)

#OPTIMIZED


def movezeros(arr):
    zero_pos=0

    for i in range(len(arr)):
        if arr[i]!=0:
            arr[zero_pos],arr[i]=arr[i],arr[zero_pos]

            zero_pos+=1

    return arr



arr=list(map(int,input().split()))
print(movezeros(arr))