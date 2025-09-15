# Solution :
def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting_correct(greeting):
        print("$0")
    elif greeting_incorrect(greeting):
        print("$20")
    else:
        print("$100")

def greeting_correct(greet):
    return greet.startswith("hello")


def greeting_incorrect(greet):
    return greet.startswith("h")

main()


# Error / Mistake programming :

def main():
    greeting = input("Greeting: ")
    if greeting_correct(greeting):
        print("$0")
    elif greeting_incorrect(greeting):
        print("$20")
    else:
        print("$100")

def greeting_correct(greet):
    correct_greet = {"hello"}
    return greet.strip() in correct_greet # Error (1)


def greeting_incorrect(greet):
    incorrect_greet = {"h"}
    return greet.strip() in incorrect_greet # Error (2)

main()

### The reason why we cannot use return function "standalone" is because return greet.strip() in correct_greet only checks the exact match / answer which is only {"hello"} ###
# It means that greet.strip() in correct_greet will only return True if the input is exactly "hello".

# "hello" → ✅ True
# "hello there" → ❌ False
# "Hello" → ❌ False (because case mismatch)

# So the logic was too strict because even though you "Hello" with capital H, it will still be wrong because it does not match the true stored data inside correct_greet which is "hello".
# We can use return function only if it's a true or false scenario/case.
# In this task, anything that starts with {hello} whether it is capitilize or small caps : it will be acceptable, same goes to anything that starts with "h" whether it is capitilize or small caps since we have .lower() function.

### That is why we need to use return .startswith() function so that anything that starts with "hello" or "h" will be acceptable and otherwise false ###
# The function startswith("hello") allows:

# "hello" ✅
# "hello there" ✅
# "Hello" ✅ (if you first .lower() the string)

### Conclusion ###
# 1. Use return function "standalone" only if the answer in the case/task are fixed answers/data. return function is used for true or false scenario/case. return function is used in strict case (it can only acccept fixed answers/data only).
# 2. Use return .startswith() function if the correct answer for the case/task begins with a certain letters or words (e.g., "hello" or "hello there" or "h"), the answers will be acceptable instead of requiring the entire answer to be an exact match. If it requires to be an exact match, then use return function.
# 3. return .startswith() function is more lenient. It basically means return true if the input anwsers starts with a certain letter or words and accept it.