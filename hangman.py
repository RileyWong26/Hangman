from pickle import GLOBAL
from tabnanny import check
from wsgiref.util import guess_scheme

import requests
import random

WORDSITE = "https://www.mit.edu/~ecprice/wordlist.10000"
RESPONSE = requests.get(WORDSITE)
WORDS = RESPONSE.content.splitlines()
WORD = str(random.choice(WORDS)).replace("'", "")[1:]
guessed = []

counter = 0
def checkGuess(guess):
    for i in range(len(guessed)):
        if guess in guessed:
            return False
    return True
def userInput():
    global guessed
    guess = input("Guess a letter: ").strip()[0].lower()
    while not checkGuess(guess):
        print("YOU ALREADY GUESSED THAT LETTER")
        guess = input("Guess a letter: ").strip()[0].lower()
    guessed.append(guess)
    return guess

def word(guess):
    global updatedWord
    new = ""
    if guess in WORD:
        for i in range(len(WORD)):
            if WORD[i] == guess and updatedWord[i] == "*":
                new = new + WORD[i]
            elif updatedWord[i] != "*":
                new = new + updatedWord[i]
            else:
                new = new + "*"
        hangman(True)
    else:
        new = updatedWord
        hangman(False)
    return new

def hangman(error):
    global counter
    if error:
        draw(counter)
    else:
        counter +=1
        draw(counter)
    pass
def draw(counter):
    if counter >= 0:
        print("         |")
    if counter >= 1:
        print("         O")
    if counter >= 2:
        print("        /|", end="")
    if counter >= 3:
        print("\\")
    if counter >= 4:
        print("        /", end=" ")
    if counter >= 5:
        print("\\")
    print()
    print()
def main():
    global updatedWord
    updatedWord = word(userInput())
    return updatedWord



updatedWord = "*" * len(WORD)
print(updatedWord)

while "*" in updatedWord and counter < 5:
    print(f"YOU HAVE GUESSED: {guessed}")
    updatedWord = main()
    print(updatedWord)

if counter == 5:
    print("YOU LOSE")
    print(f'the word is : {WORD}')
else:
    print("YOU WIN")