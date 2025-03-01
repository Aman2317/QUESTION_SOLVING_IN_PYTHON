# Print multiplication table of the x (Input taken from user).
# The formate of table should be in e.g. 2 x 2 = 4.

print("Hello! This Program will Print Multiplication Table")

# To take input inpu from user to print table.
x = int(input("Enter the number: "))


for y in range(1, 10 +1):
    z = x*y
    print(f"{x} x {y} = {z}")