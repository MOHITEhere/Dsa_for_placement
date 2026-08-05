#find lcm of 2 number 
'''lcm formula :
a*b/gcd(a,b)'''


def hcf(a,b):
    while b!=0:
        a,b=b,a%b

    return a 

def lcm(a,b):
    return a*b//hcf(a,b)

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print(lcm(a,b))
