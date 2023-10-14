# 1. Randomly choose a word from the pre-defined words list, 
# display the word filling with '_'
#
# 2. Ask the gamer to guess a letter
#
# 3. If the letter belongs to the word chosen, put it in the
# corresponding place of the word, other positions stay filling
# with '_'
#
# 4. If the letter typed in does not belong to the word, draw a
# stroke towards hanging the man. After using all the opportunities,
# the game is over, and the man is hanged.

import random

words = ["pizza", "apple", "onion", "banana"]

def getRandomWord():
    return random.choice(words)

def initGlobalVariables():
  global lettersTyped, randomWord, wordToDisplay, letterLeftCount, errorCount, totalOpportunities
  lettersTyped = []
  randomWord = getRandomWord()
  wordToDisplay = len(randomWord) * '_'
  letterLeftCount = len(randomWord)
  errorCount = 0
  totalOpportunities = 6

def replaceWordWithCorrectLetter(wordToDisplay, correctWord, correctLetter):
  tempWord = ""
  replacedLetterCount = 0
  for i in range(len(correctWord)):
    if correctWord[i] == correctLetter:
      tempWord = wordToDisplay[:i] + correctLetter + wordToDisplay[i+1:]
      wordToDisplay = tempWord
      tempWord = ""
      replacedLetterCount += 1
  return wordToDisplay, replacedLetterCount

def tryAgain():
  return input("Try one more time? y/n: ", ).lower() == "y"

def drawHangman(guess):
  if guess == 0:
    print( "________      ")
    print( "|      |      ")
    print( "|             ")
    print( "|             ")
    print( "|             ")
    print( "|             ")
  elif guess == 1:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|             ")
    print( "|             ")
    print( "|             ")
  elif guess == 2:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|     /       ")
    print( "|             ")
    print( "|             ")
  elif guess == 3:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|     /|      ")
    print( "|             ")
    print( "|             ")
  elif guess == 4:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|     /|\     ")
    print( "|             ")
    print( "|             ")
  elif guess == 5:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|     /|\     ")
    print( "|     /       ")
    print( "|             ")
  else:
    print( "________      ")
    print( "|      |      ")
    print( "|      0      ")
    print( "|     /|\     ")
    print( "|     / \     ")
    print( "|             ")
    print( "GAME OVER!")

def displayCurrentWord():
  print(str(letterLeftCount), "letters left: ")
  print(wordToDisplay)
  drawHangman(errorCount)

initGlobalVariables()
displayCurrentWord()

while (True):
  inputLetter = input("Please guess a letter: ").lower()
  if inputLetter not in 'abcdefghijklmnopqrstuvwxyz':
    print(inputLetter + " is not a letter.")
    continue
  if inputLetter in lettersTyped:
    print("Repeated letter, try a different one.")
    continue
  else:
    lettersTyped.append(inputLetter);
    if inputLetter in randomWord:
      result = replaceWordWithCorrectLetter(wordToDisplay, randomWord, inputLetter)
      wordToDisplay = result[0]
      letterLeftCount -= result[1]
      if letterLeftCount == 0 :
        print ("Congratulations!")
        if tryAgain():
          initGlobalVariables()
        else:
          break;
    else:
      errorCount += 1
      if errorCount >= totalOpportunities:
        print("Game Over.")
        if tryAgain():
          initGlobalVariables()
        else:
          break;
    displayCurrentWord()