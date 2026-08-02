class Count:
    def counting_digits(self,num):
        num=abs(num)
        if num==0:
            return 1
        count=0
        while num>0:
            count+=1
            num=num//10

        return count



num=int(input())
ans=Count()
result=ans.counting_digits(num)
print(result)