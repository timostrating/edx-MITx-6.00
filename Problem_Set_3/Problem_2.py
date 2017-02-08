def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    outputString = ""

    for v in secretWord:
        flag = False
        for l in lettersGuessed:
            if v == l:
                flag = True

        if flag:
            outputString += v
        else:
            outputString += "_ "

    return outputString

print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))