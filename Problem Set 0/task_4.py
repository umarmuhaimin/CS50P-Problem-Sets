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