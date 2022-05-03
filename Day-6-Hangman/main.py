from replit import clear
import random
import hangman_words
import hangman_art

play_again = True

while play_again:
    clear()
    print(hangman_art.logo)
    print("Welcome to Hangman.\nWhere ever choice is life or death.\n")
 
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    display = []
    for letter in range(word_length):
        display += "_"

    end_of_game = False
    lives = 6

    letters_guessed = []

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess not in letters_guessed:
            letters_guessed += guess
                
        clear()

        if guess in display:
            print("This letter has already been selected.\nPlease choose another letter.\n")

        if guess in chosen_word:
            if guess not in display:
                print("Good guess. This letter is in the word.\n")
            
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter
            
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}. This character is not in the word. You lose a life.\nRemaining lives: {lives}.\n")
            
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}.\n")

        if "_" not in display:
            end_of_game = True
            print("Congratulations. You win!\n\n")
        
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        print(f"Letters already guessed:\n{letters_guessed}\n")

        if end_of_game == True:
            print("Do you want to play again?")
            restart = input("Type 'yes' or 'no': ")
            if restart == 'no':
                play_again = False
                print("\nThank you for playing.")
        

        










