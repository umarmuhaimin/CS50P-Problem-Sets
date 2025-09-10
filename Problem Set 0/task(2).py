# Option 1 : using .replace() method

def playback():
    conversation = input("Can you talk a little bit slower this time? ")
    slower = conversation.replace(" ", "...") # " " means space in between words.
    print(slower)

playback() # We can run the code by calling the playback function at the end of the system.


# Option 2 :

print(input("Can you talk a little bit slower this time? ").replace(" ", "..."))


# Option 3 :

conversation = input("Can you talk a little bit slower this time? ")
print(conversation.replace(" ", "..."))


# The .replace() method replaces a specified phrase with another specified phrase. 
# .replace() method replaces all occurrences of a specified substring in a string and returns a new string without modifying the original string.
# .replace(old, new)

# for example :
#   phrase = "The sun is strong today. I don't really like sun."
#   substituted_phrase = phrase.replace("sun", "wind", 1)
#   print(substituted_phrase)
    # Output: The wind is strong today. I don't really like sun.