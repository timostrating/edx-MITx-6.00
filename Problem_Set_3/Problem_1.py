def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for v in secretWord:
        flag = False
        for l in lettersGuessed:
            if v == l:
                flag = True

        if flag:
            continue
        else:
            return False

    return True

print( isWordGuessed("", ['e', 'p', 'l', 'p', 'a', 's']) )