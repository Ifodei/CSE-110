#Guess the correct word to win the game! I added breaks to enable the player continue playing even when the 
#guess is wrong till they get it right.

def get_hint(guess, secret) :
    hint = ""

    for i in range (len(secret)) :
        if i < len(guess) and guess[i] == secret[i] :
            hint += guess[i].upper()
        elif i< len(guess) and guess[i] in secret :
            hint+= guess[i].lower()
        else :
            hint +="_"
    return hint

print("Welcome to the word Puzzle game!")
secret = "messiah"
letter_count = len(secret)
guess = ""
guess_count = 0

print("\nYour hint is :")
print("_" * len(secret))

while guess != secret :
    guess = input("What is your guess?").strip().lower()
    guess_count += 1
    if len(guess) != letter_count :
        print(f"Your guess must contain {letter_count} characters.")
        continue
    

    if guess == secret :
        print("Congratulations!You guessed right!")
        break
    else :
        print("Your guess is not correct")
        hint = get_hint(secret, guess)
        print(f"Hint ; {hint}")
        

print(f"You have guessed {guess_count} number of times.")