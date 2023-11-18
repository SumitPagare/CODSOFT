def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Select operation:")
print("+")
print("-")
print("*")
print("/")

choice = input("Enter which operator you want: ")

if choice == '+':
    result = add(num1, num2)
    operation = "+"
elif choice == '-':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '*':
    result = multiply(num1, num2)
    operation = "*"
elif choice == '/':
    result = divide(num1, num2)
    operation = "/"
else:
    print("Invalid Input")
    exit()

print(str(num1) + " " + operation + " " + str(num2) + " = " + str(result))








