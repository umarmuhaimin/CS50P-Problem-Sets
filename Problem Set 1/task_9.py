def main():
    interpreter = input("Expression: ") # Can only have 3 numerical number / operator : x, y, z = 1 + 1
    # x = int, y = op, z = int with one space in between each other.
    x, y, z = interpreter.split() # split each numerical number/operator by one space in between each other. Split into 3 parts.
    x = float(x)
    z = float(z)

    # We can use result variable. result is just a variable to store the value of the calculation. The variable can be any name to store the data.
    if y == "+": # If the operator inputed is "+", a calculation of x + z will occur, then calculated value be stored into result variable. This method also goes the same to other operator.
        result = x + z # Finally, when main() is called ; it will print the calculated value into output.
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Undefined")

    print(f"{result:.1f}") # Print the result to 1 decimal place.

main()