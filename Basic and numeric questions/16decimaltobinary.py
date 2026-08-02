#binary to decimal and decimal to binary 

def binary_to_decimal(n):

    n=str(n)
    power=0
    total=0

    for i in reversed(n):
        total+=int(i)*(2**power)
        power+=1

    return total

n=int(input("Enter the binary number: "))
print(binary_to_decimal(n))

def decimal_to_binary(n):
    if n == 0:
        return "0"

    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    return result

n = int(input("Enter decimal number: "))
print(decimal_to_binary(n))