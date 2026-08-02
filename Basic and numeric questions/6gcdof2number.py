class Gcd:
    def gcd_of_2number(self,a,b):

        while b:
            a,b=b,a%b
        return a 

a=int(input())
b=int(input())

ans=Gcd()
result=ans.gcd_of_2number(a,b)
print(result)