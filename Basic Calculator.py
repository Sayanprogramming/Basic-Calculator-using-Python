print("1. Addition: ")
print("2. Subtraction: ")
print("3. Multiplication: ")
print("4. Division: ")
chooseoption = int(input("Choose An Option Provided Above: "))
result = 0

if chooseoption in (1, 2, 3, 4):
    number1 = float(input("Enter The First Number: "))
    number2 = float(input("Enter The Second Number: "))
    
    if chooseoption == 1:
        result = number1 + number2
    elif chooseoption == 2:
        result = number1 - number2
    elif chooseoption == 3:
        result = number1 * number2
    elif chooseoption == 4:
        if number2 != 0:
            result = number1 / number2  # Use single slash for floating-point division
        else:
            print("Error: Division by zero is not allowed.")
            result = None
else:
    print("Invalid Option Chosen")

if result is not None:
    print("The Result of the Operation is: {}".format(result))
