import random

def randomWordFunction():
 wordToGuessList = ['flower','houses','chairs','orange']
 wordIndexValue = random.randint(0,len(wordToGuessList)-1)
 wordChoice = wordToGuessList[wordIndexValue]
 return wordChoice

def calcBulls(guessedWord):
 bulls = 0
 for letter in range(len(guessedWord)):
   if guessedWord[letter] == wordToGuess[letter]:
     bulls += 1
 return bulls

def calcCows(guessedWord):
 cows = 0
 for letter in range(len(guessedWord)):
   if guessedWord[letter] in wordToGuess and guessedWord[letter] != wordToGuess[letter]:
     cows += 1
 return cows

def turnManagement():
 turns = 5
 return turns

def gameIntro():
 print('Welcome! Are you smart enough to guess the 6-letter hidden isogram? There\'s only one way to find out! \nYou\'ll gain one bull by guessing a letter on the same spot as in the pre-defined word. \nIf the letter you guessed is in the word but not in the exact same spot as in the pre-defined word, you\'ll gain one cow. \nTry guessing the word in max. 5 turns! The best of luck! \r\b')

def winning(valBulls):
 if valBulls == len(wordToGuess):
   print('\rGreat job! Thanks for playing :)')
   exit()

def gamePlay(calcBulls,calcCows,winning,turn):
 for turn in range(turn, 0, -1):
   guessedWord = input('Enter a word: ')
   valBulls = calcBulls(guessedWord)
   valCows = calcCows(guessedWord)
   winner = winning(valBulls)
   if winner == True:
     winning(valBulls)
     exit()
   else:
     print('You gained ', valBulls, ' bulls in your guess')
     print('You gained ', valCows, ' cows in your guess')


wordToGuess = randomWordFunction()
startIntro = gameIntro()
turns = turnManagement()
startGame = gamePlay(calcBulls,calcCows,winning,turns)
