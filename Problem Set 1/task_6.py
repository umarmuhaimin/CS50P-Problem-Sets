# Option (1) :
def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    if verify_answer(answer):
        print("Yes")
    else:
        print("No")

def verify_answer(ans):
    correct_answers = {"42", "forty-two",
    "forty two"}
    return ans.strip().lower() in correct_answers  # Always remember to use "return" to check whether the inputed data is true using "return function" otherwise it is false.
                                                   # standalone "return" in this line of code means return true if the value of input ans == correct_answer stored data variable.
main() # No need to do {return true and return false}. If ans == correct_answers, then it will return true, otherwise return false automatically without mentioning return true or return false. "return" at this line of code directly means return true only for the fixed answers.
       # .strip() and .lower() are needed to make sure that there are no spaces left and all words are lowered to match the correct_answers.


# Option (2) :
def main():
    answer = input()
    if correct_answer(answer):
        print("Yes")
    else:
        print("No")

def correct_answer(ans):
    confirmed_answer = {"42", "forty-two", "forty two"}
    return ans.strip().lower() in confirmed_answer # return true if ans from user's input is inside confirmed_answer stored data. Otherwise, return false and print "No".

main()


# Before fixing the error and explaination :
def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    if verify_answer(answer):
        print("Yes")
    else:
        print("No")

def verify_answer(ans):
    ans = {"42", "forty-two",
    "forty two"}

main()

# Your function verify_answer does not actually check if the user's answer matches any of the correct answers.
# Instead, it just reassigns ans to a set and does not return anything, so it always returns None (which is treated as False).
# How to fix: You should check if the input is in the set and return True or False.