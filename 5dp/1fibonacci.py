#fibonacci series 
class Fibonacci:
    def fibonacci_series(self,n):
        if n<=1:
            return n 
        
        dp=[0]*(n+1)

        dp[0]=0
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
    



n=int(input())
ans=Fibonacci()
result=ans.fibonacci_series(n)
print(result)