'check whether the number is prime or composite'

class Check:
    def prime(self,n):
        if n<=0:
            return -1 
        if n==1:
            return "Nor composite not prime"
        if n==2:
            return "Prime"
        elif n%2==0:
            return "Composite"
        for i in range(3,int((n**0.5)+1),1):
            if n % i ==0:
                return "Composite"
        
            return "prime"

n=int(input())
ans=Check()
result=ans.prime(n)
print(result)