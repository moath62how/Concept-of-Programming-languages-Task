from random import choice,shuffle
predefined_words = ["Apple", "Dog" , "Banana", "Ship","Carrot"]
random_word = choice(predefined_words)
random_word_shuffled = list(random_word)
shuffle(random_word_shuffled)
random_word_shuffled = "".join(random_word_shuffled)
while random_word_shuffled == random_word:
    random_word_shuffled = list(random_word)
    shuffle(random_word_shuffled)
    random_word_shuffled = "".join(random_word_shuffled)

attempts= 5
print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original word from the scrambled word: {random_word_shuffled}")
print(f"You have {attempts} attempts.")
while attempts > 0:
    user_try = input("Enter your guess:").lower().strip()
    if user_try == random_word.lower():
        print("Congratulations! You guessed the correct word!")
        break
    elif user_try == "":
        print("error: you must enter a guess")    
    else:
        attempts-=1
        print(f"Incorrect! Try again. You have {attempts} attempts left.")
if attempts == 0:
    print(f"You're out of attempts! The correct word was: {random_word}")
