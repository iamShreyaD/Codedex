#Create a calculator.py program and define these five functions:

#add(a, b) that adds two numbers a and b.
#subtract(a, b) that subtracts two numbers a and b
#multiply(a, b) that multiplies two numbers a and b.
#divide(a, b) that divides two numbers a and b.
#exp(a, b) that takes a to the exponent (or power) of b.
#Make sure to return the result in each function definition.

x = int(input("Enter digit 1: "))
y = int(input("Enter digit 2: "))

def add(a, b):
      return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    return a ** b

print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))
print(exp(x, y))