def main():
    time = input("What time is it? ")
    time = convert(time) # time variable also stores convert(time) function.

    if breakfast_times(time):
        print("breakfast time")
    elif lunch_times(time):
        print("lunch time")
    elif dinner_times(time):
        print("dinner time")


def breakfast_times(time): # return true for breakfast_times if time is in between 7 and 8.
        return 7 <= time <= 8

def lunch_times(time):
        return 12 <= time <= 13

def dinner_times(time):
        return 18 <= time <= 19


def convert(time):  # Before we can convert into integer, we need to identify hours and minutes. So use .split()function to remove (":") and identify the strings of hours and minutes.
    hours, minutes = time.split(":") # To split the single string of "7:30" into two strings --> ["7", "30"] and assigns it as [hours, minutes]. so hours = "7" and minutes = "30". The string of 7 is inside hours variable and string of 30 is inside minutes variable.
    hours = int(hours) # Convert strings into integer.
    minutes = int(minutes) # Convert strings into integer.
    return hours + minutes / 60 # return true if the user's input meets the criteria of this function to convert the input into a proper decimal number by calculation.

if __name__ == "__main__":
    main()


# The reason why .split(":") is needed in hours, minutes = time.split(":") is because :

# 1. the user’s input comes in a string format like "7:30" because it uses input() function. RECALL : input returns a string.
# 2. "7:30" is not two separate numbers — it’s just text.
# 3. .split(":") tells Python to cut the "7:30" string wherever it sees ":".
# 4. So "7:30" string will be splitted into two different string → ["7", "30"].
# 5. Then we assign: hours = "7" and minutes = "30"
# 6. After that, we convert them into integers:
   # hours = int(hours)       # the string of "7" stored inside hours variable will be converted into integer of 7.
   # minutes = int(minutes)   # the string of "30" stored inside minutes variable will be converted into integer of 30.
# 7. This way, we can turn the input into a proper decimal number:
                     # 7 + 30/60 = 7.5

### Without .split(":"), Python wouldn’t know how to separate hours from minutes ###
### in order to remove something permanently inside a string, you can use .split("") function ###
### "7" and "30" are strings | 7 and 30 are integers ###