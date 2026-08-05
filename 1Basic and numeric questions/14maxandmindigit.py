#return the maximum and minimum digit in the number
def max_min_digit(n):
    max_digit=0
    min_digit=9

    while n>0:
        x=n%10

        if x>max_digit:max_digit=x
        if x<min_digit:min_digit=x

        n=n//10

    return min_digit,max_digit


n=int(input())
print(max_min_digit(n))