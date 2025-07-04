# Take user input and check if the number is a perfect square.

n = int(input("Enter a number: "))
print(n)

flag = 0

if n == 0:
    flag = 1  # 0 is a perfect square (0 * 0 = 0)
else:
    for i in range(0, n + 1):  # Loop should go up to n (inclusive) .i.e; writting (n + 1) as the end enables us to include the value stired in n. And in case of 
        if i * i == n:
            flag = 1
            break

if flag:
    print("perfect sq.")
else:
    print("not perfect sq.")
