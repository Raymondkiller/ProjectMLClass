import random
import sys

# Input
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

# Func
def drinkRadum(_drink):
    return random.choice(_drink)

def answersQues(_inString):
    print(_inString + " [y/n] ")
    while True:
        _input = input()
        if (_input.upper() == 'YES') | (_input.upper() == 'Y'):
            return True
        elif (_input.upper() == 'NO') | (_input.upper() == 'N'):
            return False
        else:
            print("Please respond with 'yes' or 'no' or 'y' or 'n'.")
            continue

# Run
print("Nice to meet you, pls choose your drink!")
drinkOder = ""
for drink in questions:
    if answersQues(questions[drink]):
        _choice = drinkRadum(ingredients[drink])
        print("i choice",_choice," for you!")
        drinkOder = drinkOder + _choice + " and "

print("Your oder is:", drinkOder[:len(drinkOder)-5])
