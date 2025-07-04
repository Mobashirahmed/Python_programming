inputNumber = int(input("Enter a number: "))
square = inputNumber * inputNumber
turn = 10

# Store the original number for final comparison
originalNumber = inputNumber
flag = False

# Loop to check if the last digits of the square match the original number
while inputNumber > 0:
    remainder = square % turn
    if remainder == originalNumber :
        flag = True
        break
    inputNumber = inputNumber // 10
    turn = turn * 10
    
if flag:
    print(originalNumber, " is an Automorphic number.")
else:
    print(originalNumber, " is not Automorphic number.")



#     if square % 10 == inputNumber % 10:
#         # Remove the last digit of both the square and the number
#         square = square % 10
#         inputNumber = inputNumber // 10
#     else:
#         # If at any point the digits don't match, it's not an Automorphic number
#         print(originalNumber, ", It is not Automorphic.")
#         break
# else:
#     # If the loop ends and no mis-match occurs, it is Automorphic
#     print(originalNumber, ", It is Automorphic.")