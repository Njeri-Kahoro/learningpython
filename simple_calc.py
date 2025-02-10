num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")


#perform the calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num1 != 0:
     result = num1 / num2
    else:
        result = 'Error! Division by zero!'
else:
    result = 'Invalid operator!'
print(f'The result is : {result}')
