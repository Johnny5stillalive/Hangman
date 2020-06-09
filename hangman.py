import random

# Write your code here
word_file = "dic"
words = open(word_file).read().splitlines()
#words = ["python", "java", "kotlin", "javascript"]
playing = True

while playing:
    word = random.choice(words)
    word2 = list(len(word) * "-")
    tries = 8
    guesses = 0
    letter_list = []
    print("H A N G M A N")
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
            if letter_guess == "exit":
                break
            elif not letter_guess.islower():
                print("It is not an ASCII lowercase letter.")
            elif len(letter_guess) > 1:
                print("You should input a single letter.")
            elif letter_guess in letter_list:
                print("You already typed this letter.")
            elif letter_guess not in word:
                print("No such letter in the word.")
                guesses += 1
            for letter in word:
                if letter == letter_guess:
                    word2[i] = letter_guess
                i += 1

            if word == "".join(word2):
                print(f"Your guessed the word: {word}")
                print("You survived!")
                break

            if guesses == tries and word != word2:
                print(f"The word was {word}")
                print("You are hanged!\n")
            if letter_guess not in letter_list and letter_guess.islower() and not len(letter_guess) > 1:
                letter_list.append(letter_guess)

    elif answer == "exit":
        break