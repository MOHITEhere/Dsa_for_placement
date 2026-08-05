
# Check if a number can be expressed as sum of two Prime Numbers


# Given a number n, the task is to check if it is possible to express n as the
#  sum of two prime numbers, a and b. If such pair does not exist, return [-1, -1].

# Note: If [a, b] is one solution with a <= b, and [c, d] is another solution with 
# c <= d, and a < c then  [a, b] is considered as our answer.

# Examples: 
# Input: n = 19
# Output: Yes
# Explanation: The number 19 can be written as 17 + 2, here 17 and 2 are both primes.

# Input: n = 14
# Output: Yes
# Explanation: The number 14 can be written as 7 + 7.

# Input: n = 11
# Output: No


class Sumof2primenumber:
    def prime(self,n):
        
        if n==2:
            return True
        elif n%2==0:
            return False
        for i in range(3,int((n**0.5)+1),1):
            if n % i ==0:
                return True
        
        return False
    
    def prime_sum(self,n):
        answer=[]
        for i in range(2,(n//2)+1):
            if self.prime(i)+self.prime(n-i)==n:
                answer.append([i,n-1])

        return answer
                
    
n=int(input())
ans=Sumof2primenumber
result=ans.prime_sum(n)
print(result)