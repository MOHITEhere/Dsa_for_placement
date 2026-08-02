#Sum of AP Series 
def apseries(a,d,n):
    sum=n*(2*a+(n-1)*d)//2
    return sum 

a=int(input("Enter the first term: "))
n=int(input("Enter number of terms: "))
d=int(input("Enter the difference: "))
print(apseries(a,d,n))