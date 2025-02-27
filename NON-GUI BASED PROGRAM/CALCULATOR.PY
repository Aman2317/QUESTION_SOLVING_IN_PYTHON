# Making a calculator

# Please select operation -
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Select operations form 1, 2, 3, 4 : 1
# Enter first number : 15
# Enter second number : 14
# 15 + 14 = 29


print("Please select operation - \n" \
    "1. Add(+) \n"
    "2. Subtract(-) \n"
    "3. Multiply(*) \n"
    "4. Divide(%) " )

operation = int(input("Select operation from 1, 2, 3, 4 : "))

if operation not in [1, 2, 3, 4]:
    print("Please select from the given range of operation")

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if operation == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == 4:
    print(f"{num1} % {num2} = {num1 % num2}")