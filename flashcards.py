"""
Flashcard app Prototype 1
How it should work: 
1. Read Flashcard string from a text file
2. Randomize the order of the string
3. Print the Flashcards one by one and wait for user's response
4. Show correct answer after user response
"""

def flashcards(file):
    flashc = open(file, "r")
    print(flashc.read())

flashcards('flashcard_list.txt')
