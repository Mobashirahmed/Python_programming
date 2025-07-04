# Take user input and check if the number is a perfect square.

print("Enter a number: ")
x = int(input())
print(x)

flag = False

for i in range(1, x):
    if i*i == x:
        flag = True
        break

if flag :
    print("We've a perfect sq. number")
else:
    print("It is not perfect sq. number")