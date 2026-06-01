import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_diffultiy(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right... the answer was {answer}")

print(logo_art.logo)
print("let me think of a number between 1 to 50.")
answer=random.randint(1,50)
print(answer)
level=input("choose level of difficulity....type'easy' or 'hard': ")
attempt=set_diffultiy(level)
guessed_number=0
while guessed_number!=answer:
      print(f"you have {attempt} remaning to guess the number.")
      guessed_number=int(input("guess a number:"))
      attempt=check_answer(guessed_number,answer,attempt)
      if attempt==0:
          print("you are out of guesses.... you lose!")
      else:
          print("Guess again")    
          