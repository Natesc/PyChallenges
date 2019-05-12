import random

# Rock Paper Scissors Game
# Goals: Greet the player, respond if they win/lose


# Rock Paper Scissors Game
def rps():
    # Define Basic Variables
    play_again = True
    wins = 0
    losses = 0
    ties = 0

    rock = 'rock'
    scissors = 'scissors'
    paper = 'paper'

    # Define the choices and put them into a list
    choices = [rock, paper, scissors]

    print("Hello! Welcome to Rock Paper Scissors")

    # While Playing Ask for the users choice
    while play_again:
        player_Choice = input("\nPlease choose rock, paper, or scissors: ")

        # Make sure the choice is valid
        while player_Choice.lower() not in choices:
            player_Choice = input("\nInvalid choice, please choose rock, paper, or scissors: ")

        # Computer makes a choice
        pc_choice = random.randint(1, 3)
        if pc_choice == 1:
            pc_choice = rock
        elif pc_choice == 2:
            pc_choice = paper
        else:
            pc_choice = scissors

        # If they are the same Tie
        if player_Choice.lower() == pc_choice:
            print("\nYou tied!")
            ties += 1

        # If the players choice beats the computers choice Win
        elif (player_Choice.lower() == rock and pc_choice == scissors) or (player_Choice.lower() == scissors and pc_choice == paper) or (player_Choice.lower() == paper and pc_choice == rock):
            print("\nYou win!")
            wins += 1

        # Else Lose
        else:
            print("\nYou lose!")
            losses += 1

        # Ask the user if they would like to play again and make sure they say yes or no
        again = input("\nWould you like to play again? ")

        while again.lower() not in ('yes', 'no'):
            again = input("Invalid input please choose Yes or No: ")

        # If the answer is no print the number of wins, losses, and ties and stop playing.
        if again.lower() == 'no':
            total = ['Wins: ' + str(wins), 'Losses: ' + str(losses), 'Ties: ' + str(ties)]
            print('\n' + '\n'.join(total))
            play_again = False


# Hangman Game
def hangman():
    # Define the word list and other basic variables
    play_again = True
    word_list = ['Banana', 'Apple', 'Orange', 'Grape', 'Pineapple']
    tried = []
    guesses = 0
    print("Welcome to the Hangman Game\n")

    # While the user is playing run the game
    while play_again:
        # Pick a word from the word list convert it into a lowercase version and define the length of chosen word
        word = random.randint(0,len(word_list)-1)
        word = word_list[word].lower()
        newlen = len(word)

        # Tell the user the length of the word.
        print("The length of the word is: " + str(len(word)))

        # While user has guesses and the word isn't complete ask for more guesses
        while guesses < 6 or newlen != 0:
            user_guess = input('\nGuess a letter in the word: ')

            # Check to make sure they haven't already guessed the letter they chose if they did give them another try
            while user_guess.lower() in tried:
                user_guess = input("\nYou already guessed that letter, try again: ")

            # Append the letter they chose to the list of chosen letters
            tried.append(user_guess.lower())

            # Make sure they only choose 1  letter
            while len(user_guess) != 1:
                user_guess = input('\nPlease guess a single letter: ')

            # If the letter isn't in the word tell them and remove a guess
            if user_guess.lower() not in word:
                guesses += 1
                print("Letter not in word you have " + str(6-guesses) + " tries left")

            # If the letter is in the word find out how many times it appears
            # Then let the user know how many times it appears and how many letters are left.
            else:
                num = len([i for i in word if i.lower() == user_guess.lower()])
                print("\nThe letter " + user_guess + " shows up " + str(num) + " times in the word")

                # Remove the letter(s) from the length of the word
                newlen = newlen - num
                print("There are " + str(newlen) + " letters left in the word")

            # If the user guessed all of the letters they win
            if newlen == 0:
                print('\nCongratulations, you guessed the word ' + word.capitalize())
                break

            # Else if they run out of tries the man hangs.
            elif guesses >= 6:
                print("\nYou guessed wrong and the man was hung...")
                break

        # Ask them if they would like to play again and make sure they say yes or no
        choice = input("\nWould you like to play again? (Yes or No): ")

        while choice.lower() not in ('yes', 'no'):
            choice = input("\nPlease choose either Yes or No: ")

        if choice.lower() == 'no':
            play_again = False

        # If they say yes remove the tried letters and set the guesses back to 0
        else:
            tried = []
            guesses = 0
            play_again = True


# Guess the Number Game
def guess_number():
    # Welcome the user and define basic variables
    tries = 6
    playing = True
    pc_num = random.randint(0, 50)
    print("Welcome to Guess the Number!")

    # While the user is playing check if they have used all of their tries
    # If they have tell them and ask if they want to play again
    while playing:
        if tries <= 0:
            if tries == 0:
                choice = input("\nYou ran out of tries! Would you like to play again? (Yes or No): ")

                while choice.lower() not in ('yes', 'no'):
                    choice = input("\nInvalid input please choose Yes or No: ")

                # If they are playing again set the # of tries back to 6 and generate a new number
                if choice.lower() == 'yes':
                    tries += 6
                    pc_num = random.randint(0, 50)
                else:
                    playing = False
                    break

        # If the user has tries print the number they have and ask them to pick a number
        print("\nYou have " + str(tries) + " tries")
        guess = int(input("Pick a number between 0 and 50: "))

        # Make sure the guess is within the given range
        while guess < 0 or guess > 50:
            guess = int(input("Invalid number. Please choose a number between 0 and 50: "))

        # If they guess the number tell them and then ask if they would like to play again
        if guess == pc_num:
            print("\nYou successfully guessed the number!")

            choice = input("\nWould you like to play again? (Yes or No): ")

            while choice.lower() not in ('yes', 'no'):
                choice = input("\nInvalid input please choose Yes or No: ")

            # If they're playing again generate a new number
            if choice.lower() == 'yes':
                pc_num = random.randint(0, 50)
            else:
                playing = False

        # If they didn't guess the number tell them if they are higher or lower than the number
        elif guess > pc_num:
            tries -= 1
            print("\nYou guessed to high!")
        else:
            tries -= 1
            print("\nYou guessed to low!")
