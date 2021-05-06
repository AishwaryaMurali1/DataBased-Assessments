"""
This function factorial takes a parameter k and
returns the factorial of that number.
Here I have made use of a dictionary to store the
number as key and it's factorial as the corresponding value.
This is done in order to reduce the computing by using memoization 
and the formula that n! = n*(n-1)!
"""
factorial_memo = {}
def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]

"""
This function leastFactorial takes a parameter n 
and returns the smallest factorial k greater than n.
I have called the function factorial() to get the 
factorial of the number.
"""

def leastFactorial(n):
    k = 0                      
    for i in range(1,n+1):
        k = factorial(i) 
        if k>n:
            return k
    return k+1