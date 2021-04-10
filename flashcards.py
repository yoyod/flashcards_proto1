"""
Flashcard app Prototype 1
How it should work: 
1. Read Flashcard string from a text file
2. Randomize the order of the string
3. Print the Flashcards one by one and wait for user's response
4. Show correct answer after user response
"""

def flashcards(file):
    # The next five lines build a list out of the text file
    flashc_raw = open(file, "r")
    flashc = flashc_raw.read()
    flashc_list = flashc.split(" ")
    flashc_raw.close()

    # The list contains spanish words at even indexes and english words at odd indexes. We separate them into two lists.
    spanish = flashc_list[::2]
    english = flashc_list[1::2]
    print(spanish)
    print(english)

    # Here we still need to randomly rearange the cards in the lists
    random_spanish = spanish
    random_english = english

    # Print the cards one by one and wait for the answer
    for w in random_spanish:
        print(w)
flashcards('flashcard_list.txt')
