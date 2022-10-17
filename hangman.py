#----------Imports-----------
import random
from dictionary import word_list
from art import logo, stages


#----------Variables-----------
#Get a random word
chosen_word = random.choice(word_list)
#Get the length of the word
word_length = len(chosen_word)
#Track End of Game
end_of_game = False
#Track Lives
lives = 6
#Print the logo
print(logo)
#Testing code - uncomment to see word at start of game
#print(f'Pssst, the solution is {chosen_word}.')


#-----------Functions-----------
#Populate the initial word display
def populate_display():
    display = []
    for _ in range(word_length): #note use of underscore for unused looping var
        display += "_"
    return display

#Return boolean if letter has already been guessed
def check_if_already_guessed(word_display, guessed_letter):
    return guessed_letter in word_display

#Update the display if a letter in the word is guessed
def update_display_if_correct(guessed_letter, display_letters):
    for position in range(word_length): #axiom => [0,1,2,3,4]
        #get letter at that position
        letter = chosen_word[position]
        #check if letter equals guessed letter
        if letter == guessed_letter:
            display_letters[position] = letter
    return display_letters

#Check the amount of lives the player has
def check_lives(guessed_word, lives):
    if guessed_word not in chosen_word:
            print(f"You guessed {guessed_word}, that's not in the word. You lose a life.")
            lives -= 1
    return lives

#Check if player is out of lives
def check_game_over():
            return lives == 0

#Return the display formatted without dashes or brackets
def get_formatted_display(display):
        return f"{' '.join(display)}"


#Populate the display before the game loop
display = populate_display()

#----------Game Loop------------
while not end_of_game:
    
    #Get Player's Guess
    guess = input("Guess a letter: ").lower()
    
    #Check if letter is already guessed
    if check_if_already_guessed(display, guess):
        print(f"You've already guessed '{guess}'")

    #Update display if letter guessed is correct
    display = update_display_if_correct(guess, display)

    #Reset the number of lives
    lives = check_lives(guess, lives)

    #Print amount of lives left
    print(f"You have {lives} lives left")
    #Join all the elements in the list and turn it into a string
    
    #Print new display
    print(get_formatted_display(display))

    #Check if user is wrong
    if check_game_over():
        print("YOU LOSE!")
        end_of_game = True
        print(stages[lives])
        break

    #Check if user has got all letters
    if "_" not in display:
        print("YOU WIN!")
        end_of_game = True
        break
    
    #Print the stage the hangman is at
    print(stages[lives])

