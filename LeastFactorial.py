factorial_memo = {}
def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]

def leastFactorial(n):
    k = 0
    for i in range(1,n+1):
        k = factorial(i)
        if k>n:
            return k
    return k+1

print(leastFactorial(106))