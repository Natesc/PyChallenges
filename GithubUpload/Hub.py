import Games

playing = True

while playing:
    options = '\nHangman\nRock Paper Scissors\nGuess the Number'
    option_list = ['hangman', 'rock paper scissors', 'guess the number']

    game_choice = input("Welcome to the game hub!\n\nPlease select a game: " + options + "\n")

    while game_choice.lower() not in option_list:
        game_choice = input("\nThat's not an option please choose one of " + options + "\n")

    if game_choice.lower() == 'rock paper scissors':
        Games.rps()
    elif game_choice.lower() == 'hangman':
        Games.hangman()
    else:
        Games.guess_number()

    choice2 = input("\nWould you like to play a different game? (Yes or No): ")

    while choice2.lower() not in ('yes', 'no'):
        choice2 = input("\nInvalid answer please choose yes or no: ")

    if choice2.lower() != 'no':
        pass
    else:
        quit()

quit()