# Speed of light constant
C = 300000000

# Einstein formula inputs
def main():
    m = int(input("What is the mass of the object / system? "))
    E = energy(m)
    print(E)

# Einstein formula calculation and squared function
def energy(mass):
    return mass * square(C)

def square(n):
    return n * n

main()

# REMEMBER, everytime you cross a situation / task that requires square, cubic or to the power of n ; you need to you the square/cubic/power function.
# In this case, always remember to define either variable function or numerical {such as squared} function in order to execute it.

# Second Method : Easy method

def main():
    m = int(input("m:"))
    C = 300000000
    E = m * C ** 2 # Note : C ** 2 means C^2
    print(E)

main()

# Since CS50P wants a program in Python that prompts the user for mass, you need to prompt it like this int(input("m:")).
# You need to include the prompt 'Mass in any of the form you comfortable with".