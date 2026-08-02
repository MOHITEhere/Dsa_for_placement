# sort arrays of 0's 1's and 2's 

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.

# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.


class Sort:
    #this does changes outside the orignal array 
    def sort012(self,arr):
        count_0=arr.count(0)
        count_1=arr.count(1)
        count_2=arr.count(2)

        ans=[0]*count_0+[1]*count_1+[2]*count_2

        return ans 

    
    #DUTCH NATIONAL FLAG ALGORITHM
    def sorting012(self,arr):
        low=0
        mid=0
        high=len(arr-1)

        while mid<high:
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1

            elif arr[mid]==1:
                mid+=1

            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1

        return arr 


    #other style 
    def other_sort012(self,arr):
        count0=0
        count1=0
        count2=0

        for num in arr:
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else:
                count2+=1

        for i in range(len(arr)):
            if i < count0:
                arr[i]=0
            elif i< count0+count1:
                arr[i]=1
            else:
                arr[i]=2

        return arr


arr=list(map(int,input().split()))
ans=Sort()
result=ans.sort012(arr)
print(result)

