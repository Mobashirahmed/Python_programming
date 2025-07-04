# Write a Python program to find the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:    # yaha..n pe OR karna tha aur mai AND kar raha tha!
        return 1
    else:
        fact = n * factorial(n-1)
        return fact

n = int(input("Enter a number: "))
print("Factorial of ", n, " is : ", factorial(n))