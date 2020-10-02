import random
from words import word_list

def getRandom():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(displayHangman(tries))
    print(word_completion)
    print("\n",len(word)," letters")
    print("\n")

    while not guessed and tries > 0:
        guess = input("Enter your guess: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job, ", guess, " is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            print(word_completion)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(displayHangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!\n")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!\n ")

def displayHangman(tries):
    stages = [ #6 final state: head, torso, both arms, and both legs
    
                '''
                    ------------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / \\
                    |
                    |
                    -
                ''',
    
                # head, torso, both arms, and one leg
                '''
                    ------------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / 
                    |
                    |
                    -
                ''',
    
                #4 head, torso, and both arms
                '''
                    ------------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      
                    |
                    |
                    -
                ''',

                #3 head, torso, and one arm
                '''
                    ------------
                    |       |
                    |       O
                    |      \|
                    |       |
                    |      
                    |
                    |
                    -
                ''',

                #2 head and torso
                '''
                    ------------
                    |       |
                    |       O
                    |       |
                    |       |
                    |      
                    |
                    |
                    -
                ''',

                #1 head
                '''
                    ------------
                    |       |
                    |       O
                    |      
                    |       
                    |      
                    |
                    |
                    -
                ''',

                #0 initial empty state
                '''
                    ------------
                    |       |
                    |       
                    |      
                    |       
                    |      
                    |
                    |
                    -
                '''


    ]
    return stages[tries]

def main():
    word = getRandom()
    #print(word)
    play(word)

    while input("Do you want to play again(Y/N): \n").upper() == 'Y':
        word = getRandom()
        play(word)

if __name__ == "__main__":
    main()