#Check perfect number

# Input: n = 15
# Output: false
# Explanation: Divisors of 15 are 1, 3 and 5. Sum of divisors is 9 which is not equal to 15.

# Input: n = 6
# Output: true
# Explanation: Divisors of 6 are 1, 2 and 3. Sum of divisors is 6.
def check_perfect_number(n):
    if n<=0:
        return False

    count= 0
    
    for i in range(1,(n // 2)+ 1):
        if n%i == 0:
            count += i

    return count==n


n = int(input())
print(check_perfect_number(n))