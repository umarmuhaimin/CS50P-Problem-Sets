# In this task, we are basically replacing emoticons to emoji, and prompt the user to input and then print the result.

def convert(emoticon): # emoticon : emoji in the type of text.
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

def main():
    users_input = input("Are you feeling happy or sad right now? ")
    print(convert(users_input))

main()

# We are basically replacing the user's input response which will be in the type of emoticon into emoji's.
# That is why the line of code : print(convert(user's_input)) 