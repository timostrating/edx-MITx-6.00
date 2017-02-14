def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = getAvailableLetters([])
    letter = ''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    while mistakesMade < 8 and not isWordGuessed(secretWord, lettersGuessed):
        print("------------")
        print("You have " + str(8 - mistakesMade) + " guesses left")
        print("Available Letters: " + availableLetters)
        letterOrig = input("Please guess a letter: ")
        letter = letterOrig.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif letter in secretWord:
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(letter)
            availableLetters = getAvailableLetters(lettersGuessed)
            mistakesMade += 1

    print("------------")
    if mistakesMade == 8:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
    else:
        print("Congratulations, you won!")