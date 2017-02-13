def getGuessedWord(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    outputString = ""

    from string import ascii_lowercase
    for c in ascii_lowercase:
        flag = False
        for l in lettersGuessed:
            if c == l:
                flag = True

        if not flag:
            outputString += c

    return outputString

print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))