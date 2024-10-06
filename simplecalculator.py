import operator
import math

no1 = int(input("Enter First No: "))
no2 = int(input("Enter Second No: "))
ch = input("Enter Choice (+, -, *, /, pow, log): ")

if ch == "+":
    res = no1 + no2
    print("Result:", res)
elif ch == "-":
    res = no1 - no2
    print("Result:", res)
elif ch == "*":
    res = operator.mul(no1, no2)
    print("Result:", res)
elif ch == "/":
    if no2 != 0:  # Handling division by zero
        res = no1 / no2
        print("Result:", res)
    else:
        print("Error: Division by zero is not allowed.")
elif ch == "pow":
    res = no1 ** no2
    print("Result:", res)
elif ch == "log":
    if no1 > 0 and no2 > 0:  # Handling invalid log inputs
        res = math.log(no1, no2)
        print("Result:", res)
    else:
        print("Error: Both numbers must be greater than zero for log.")
else:
    print("Incorrect Choice")