# Odd-even determiner

num = input("Input a number: ")  # input() takes input from user in num variable as a string

num = int(num)                   # int() converts string num into integer num

if num % 2 == 1:
    print("Number is odd.")

else:
    print("Number is even.")
