def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Task (1) :
# 1. return str from an input and then convert it to float.
# 2. remove / replace the $ : that can be done by using . replace() method

def dollars_to_float(d):
    return float((d).replace("$", ""))

# Task (2) :
# 1. return str from an input and then convert it to float.
# 2. remove / replace the % : that can be done by using . replace()
# 3. We need to convert the input of % to 2 decimal point value : % divide by 100

def percent_to_float(p):
    return float((p).replace("%", "")) / 100