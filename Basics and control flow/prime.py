# Write a Python program to check if a number is prime.

n = int(input("Enter a no. "))


if n >= 0:
    flag = True
    
    if n < 2:
        flag = False
    else:
        for i in range(2, n):
            if n % i == 0:
                # print(i)
                flag = False
                break

if flag:
    print(n, " is a prime number.")
else:
    print(n, " is not a prime number.")