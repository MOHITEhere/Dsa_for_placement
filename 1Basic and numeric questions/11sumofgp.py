def sum_gp(a, r, n):
    if r == 1:
        return a * n
    return a * (r**n - 1) // (r - 1)

a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))

print("Sum of GP:", sum_gp(a, r, n))