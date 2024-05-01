import time
import users as u
import ui
import random

global db, icons
db = u.database
icons = ui.icons

wordsFile = open("words.txt", "r")
words = wordsFile.read().split()
wordsFile.close()


def game(user, word):
    tic = time.perf_counter()
    score = 0
    wrong = 0
    word = word.upper()
    print(word)
    found = []
    print(f"Welcome {user}")
    randWordIndex = random.randint(0, len(word) - 1)
    found.append(word[randWordIndex])
    while wrong < 8:
        toShow = ""
        for i in word:
            if i not in found:
                toShow = toShow + "_ "
            else:
                toShow = toShow + f"{i} "
        print(toShow)
        if "_ " not in toShow:
            print("YOU WON THIS ROUND")
            break
        letter = input("Guess your letter: ").upper()
        if letter in word and letter not in found:
            print("\nCorrect Guess!!")
            found.append(letter)
            score = score + 1
            continue
        elif letter in word and letter in found:
            print("already guessed")
        else:
            print("\nWRONG GUESS")
            print(icons[wrong])
            wrong = wrong + 1
    toc = time.perf_counter()
    score = score * (toc - tic)
    return score


def login():
    inp = input("Enter your Username (note: names are not case sensitive): ").lower()
    if inp == "quit":
        return -2
    if inp in db:
        password = input("enter your password: ")
        if password == db[inp]["pass"]:
            print(f"WELCOME BACK!! {inp}")
            return inp
        else:
            print("Wrong Password")
            return -1
    else:
        print(f"Welcome {inp}")
        db[inp] = {}
        password = input("set your password: ")
        db[inp]["pass"] = password
        db[inp]["highscore"] = 0
        return inp


while True:
    print("NOTE: IF YOU WISH TO EXIT, ENTER QUIT ANYTIME!!")
    index = login()
    if index == -1:
        print("login again with correct password")
        continue
    elif index == -2:
        print("Ok exiting the game")
        break
    randIndex = random.randint(0, len(words))
    word = words[randIndex]
    score = game(index, word)
    if score > db[index]["highscore"]:
        print("Congrats!! You got a highscore")
        db[index]["highscore"] = score
        f = open("users.py", "w+")
        f.write(f"database = {db}")
        break
