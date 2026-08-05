#fibonacci series 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

# Fibonacci Sequence Formula
# The Fibonacci formula is used to find the nth term of the sequence when its first and second terms are given.

# The nth term of the Fibonacci Sequence is represented as Fn. It is given by the following recursive formula,

class Fibonacci:
    def series(self,n):
        if n<0:
            return []
        if n==1:
            return [0]
        
        fibo=[0,1]
        a,b=0,1

        for i in range(n-2):
            a,b=b,a+b
            fibo.append(b)

        return fibo


n=int(input())
ans=Fibonacci()
result=ans.series(n)
print(result)