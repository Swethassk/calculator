def simple_calculator():
    print("Welcome to Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is undefined.")
            result = num1 / num2
        else:
            print("Error: Invalid operator.")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid number input.")

if __name__=="__main__":
    simple_calculator()
