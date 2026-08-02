class Majority:
    def majority_element(self,arr):
        n=len(arr)

        hashmap={}

        for num in arr:
            hashmap[num]=hashmap.get(num,0)+1

        for item,count in hashmap.items():
            if count>n//2:
                return item 

        return -1 

    #famous boyre moore voting algorithm 

    def boyre_moore_voting(self,arr):

        candidate=None 
        count=0

        for num in arr:
            if count==0:
                candidate=num
                count=1

            if num==candidate:
                count+=1
            else:
                count-=1

        if arr.count(candidate)>len(arr)//2:
            return candidate 

        return None


arr=list(map(int,input().split()))
ans=Majority()
result=ans.majority_element(arr)
print(result)

