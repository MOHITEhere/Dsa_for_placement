#print the prime factor of given number 

# Input: n = 18
# Output: [2, 3, 3]
# Explanation: The prime factorization of 18 is 2*3*3.

# Input: n = 25
# Output: [5, 5]
# Explanation: The prime factorization of  25 is 5*5.


class Factor:
    def prime_factor(self,num):
        store=[]
        i=2

        while i*i<=num:
            while num%i==0:
                store.append(i)
                num=num//i

            i+=1

        if num>1:
            store.append(num)

        return store


num=int(input())
ans=Factor()
result=ans.prime_factor(num)
print(result)