#importing
from collections import Counter

#retreving wordlist from file
wordfile = open("wordlist.txt", "r")
wordlist = wordfile.read()
wordlist = wordlist.split("\n")
wordfile.close()

#setting global variables
usedletters = [""]

#defining function that finds best letter based on wordlist and usedletters
def findbestletter(wordlist):
    #setting variables
    global usedletters
    condensedwordlist = "".join(wordlist)
    foundbestletter = False
    #while loop repeats until it find best letter
    while not foundbestletter:
        #finding most common letter in all words
        res = Counter(condensedwordlist)
        res = max(res, key=res.get)
        #checking if letter has already been guessed
        if res in usedletters:
            #if letter has been used it is removed from all words
            condensedwordlist = condensedwordlist.replace(res, "")
        else:
            #adds word to "usedletters" list and returns best letter
            usedletters.append(res)
            return(res)

#defining main loop
def main():
    #setting variables
    global wordlist
    templist = []
    #user inputs length of word
    length = int(input("Length of Word:"))
    #only keeps words of correct length
    for word in wordlist:
        if len(word) == length:
            templist.append(word)
    wordlist = templist
    #main while loop
    while True:
        #user inputs all known information
        currentinfo = input("Current Info: ")
        #analyzes user input
        for charnumber in range(len(currentinfo)):
            if currentinfo[charnumber] == "_":
                #if character is blank it is ignored
                pass
            elif currentinfo[charnumber] in usedletters:
                #if character is already known all nonmatching words are removed
                templist = []
                for word in wordlist:
                    if word[charnumber] == currentinfo[charnumber]:
                        templist.append(word)
                wordlist = templist
            else:
                #otherwise all nonmatching words are removed and letter added to usedletters list
                usedletters.append(currentinfo[charnumber])
                templist = []
                for word in wordlist:
                    if word[charnumber] == currentinfo[charnumber]:
                        templist.append(word)
                wordlist = templist
        #checks if only one word is remaining
        if len(wordlist) == 1:
            #declares victory
            print(f"Found Word: {wordlist[0]}")
            quit()

        print(f"Best Guess: {findbestletter(wordlist)}")

#starts main loop
main()
