# Write a Python program to print the Fibonacci series up to n terms.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        t = fibonacci(n-1) + fibonacci(n-2) # t = n + fibonacci(n-1) is incorrect, to obtain
        return t
        
        

n = int(input("Enter the number of terms: "))

for i in range(0, n+1):
    print(fibonacci(i), ", ")