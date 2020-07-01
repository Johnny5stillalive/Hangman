import random

# Write your code here
word_file = "dic"
words = open(word_file).read().splitlines()
#words = ["python", "java", "kotlin", "javascript"]
playing = True


#loop for main hangman game
while playing:
    word = random.choice(words)
    word2 = list(len(word) * "-")
    man = [".....|......",
           ".....|......",
           ".....().....",
           ".....|......",
           "..../|\.....",
           ".....|......",
           ".....|......",
           "..../.\....."]
    tries = 8
    guesses = 0
    letter_list = []
    print("H A N G M A N")

    # First interface for playing game
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == "play":
        while guesses < tries:
            print("\n")
            print(f"You have {tries - guesses} tries left.")

            if len(letter_list) > 0:
                print(f"You have tried these letters {letter_list}")
            print("".join(word2))
            letter_guess = input("Input a letter: ")
            i = 0

            # Always checks if the user wants to exit
            if letter_guess == "exit":
                break

            # line 45 - 48 checks for correct input
            elif not letter_guess.islower():
                print("It is not an ASCII lowercase letter.")
            elif len(letter_guess) > 1:
                print("You should input a single letter.")

            # Checks if letter is in word or not
            elif letter_guess in letter_list:
                print("You already typed this letter.")
            elif letter_guess not in word:
                print("No such letter in the word.")
                guesses += 1
                # Prints hangman image
                for i in range(guesses):
                    print(man[i])
            # Prints word with guessed letters in it
            for letter in word:
                if letter == letter_guess:
                    word2[i] = letter_guess
                i += 1

            # Checks if the user has guessed the word
            if word == "".join(word2):
                print(f"You guessed the word: {word}")
                print("You survived!\n")
                break

            # Checks if the user has failed
            if guesses == tries and word != word2:
                print(f"The word was {word}")
                print("You are hanged!\n")
            if letter_guess not in letter_list and letter_guess.islower() and not len(letter_guess) > 1:
                letter_list.append(letter_guess)

    # Exits loop if exit is typed
    elif answer == "exit":
        break