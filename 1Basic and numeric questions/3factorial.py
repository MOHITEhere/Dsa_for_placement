class Calculation :
    def factorial(self,n):
        if n<0:
            return -1
        if n==0 or n==1:
            return 1
        fact=1

        for i in range(2,n+1):
            fact=fact*i

        return fact

n=int(input())
ans=Calculation()
result=ans.factorial(n)
print(result)