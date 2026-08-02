def checkleapyear(n):
    if n%100==0:
        if n%400==0:
            return "its a leap year"

        return "its a normal year"
        
    elif n%4==0:
        return "its a leap year"
    else:
        return "its a normal year"
    

n=int(input("Enter the year: "))
print(checkleapyear(n))