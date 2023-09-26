
import random
def guessing_game():
    a = random.randint(0,5)
    user_input = input("Guess an integer: ")
    user_integer = int(user_input)
    while a == a:
        if user_integer == a:
            print('Just right. You won')
            break
        elif user_integer > a:
            print('Too high')
            #a = random.randint(0,100)
            user_input = input("Guess again: ")
            user_integer = int(user_input)
        elif user_integer < a:
            print('Too low')
            #a = random.randint(0,100)
            user_input = input("Guess again: ")
            user_integer = int(user_input)

guessing_game()




