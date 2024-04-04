def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = add_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {result}")