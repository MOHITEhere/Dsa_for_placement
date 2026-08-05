#check armstrong 
# input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input: n = 9474
# Output: true
# Explanation: 94 + 44 + 74 + 44 = 6561 + 256 + 2401 + 256 = 9474

# Input: n = 123
# Output: false
# Explanation: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36


class Check:
    def check_armstrong(self,num):
        num=abs(num)
        n=len(str(num))
        temp=num

        if num==0:
            return True

        count=0
        while num>0:
            digit=num%10
            count+=digit**n
            num=num//10

        if temp==count:
            return True
        return False
        

num=int(input())
ans=Check()
result=ans.check_armstrong(num)
print(result)