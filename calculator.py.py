def add (x, y):
    return x + y 
def sub (x, y):
    return x - y
def mul (x, y):
    return x * y
def div (x, y):
    return x / y 

num1= float(input("enter first number"))
num2= float(input("entee second number"))
operation= input("Enter operation (+, -, *, /,): ")

if operation == '+' :
   print(add(num1,num2))
elif operation == '-' :
     print(sub(num1,num2))
elif operation == '*' :
     print(mul(num1,num2))
elif operation == '/' :
     print(div(num1,num2))
    
else:
     print("Invalid operation")