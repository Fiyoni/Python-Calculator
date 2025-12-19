# Calculator Application

# aa program basic calculator che
# je python ne basics use kari ne banavyo che

# Addition Function
def add(a, b):
    return a + b

# Subtraction Function
def subtract(a, b):
    return a -b

# Multiplication Function
def multiply(a, b):
    return a * b

# Division Function
def divide(a, b):
    # zero thi divison na thaye ee mate check
    if b == 0:
        return None
    return a / b


# Modulus Function 
def modulus(a, b):
    return a % b

# Power Function
def power(a, b):
    return a ** b

# Main Menu Function
def calculator():
    while True:
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your Choice: ")

        # exit option
        if choice == "7":
            print("Calculator is Closed")
            break
        
        if choice not in["1", "2", "3", "4", "5", "6"]:
            print("Invalid Choice")
            continue


        # number input with validation
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Please Enter Valid Number")
            continue

        # choice pramane operation perform karvu
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Division is not possible from zero")
                continue
        elif choice == "5":
            result = modulus(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        print("Result: ", result)


# program start karva mate function call
calculator()

