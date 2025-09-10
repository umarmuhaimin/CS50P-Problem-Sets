# Option 1 : using functions.

def indoor_voice():
    indoor_voice = input("How are you feeling right now? ")
    return indoor_voice
print(indoor_voice().lower()) # No need to put indoor_voice() at the end of the code because you already call the variable at line 4. If you add indoor_voice at line 5, it will do nothing and might cause error because you called the variable / function twice.

# Option 2 : using print method, which is the easiest one.

print(input("How are you feeling right now? ").lower()) # We have 2 function here : the first one will be inputing data from the user. The second one will be printing the data inputed by the user as an output.