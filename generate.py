from random import *

class letter():
    def __init__(self, lowerchar, upperchar, isVowel, isConsonant):
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.isVowel = isVowel
        self.isConsonant = isConsonant

global alphabet
alphabet = [letter('a', 'A', True, False),
            letter('b', 'B', False, True),
            letter('c', 'C', False, True),
            letter('d', 'D', False, True),
            letter('e', 'E', True, False),
            letter('f', 'F', False, True),
            letter('g', 'G', False, True),
            letter('h', 'H', False, True),
            letter('i', 'I', True, False),
            letter('j', 'J', False, True),
            letter('k', 'K', False, True),
            letter('l', 'L', False, True),
            letter('m', 'M', False, True),
            letter('n', 'N', False, True),
            letter('o', 'O', True, False),
            letter('p', 'P', False, True),
            letter('q', 'Q', False, True),
            letter('r', 'R', False, True),
            letter('s', 'S', False, True),
            letter('t', 'T', False, True),
            letter('u', 'U', True, False),
            letter('v', 'V', False, True),
            letter('w', 'W', False, True),
            letter('x', 'X', False, True),
            letter('y', 'Y', True, True),
            letter('z', 'Z', False, True)]

def makeName():
    min = 3
    max = 10
    nameLength = randint(min, max)

    name = ""

    prevVowel = False
    prevConsonant = False
    prev2Vowel = False
    prev2Consonant = False

    for i in range(0, nameLength):
        a = getLetter(prev2Vowel, prev2Consonant)
        if(i == 0):
            name = name + a.upperchar
        else:
            name = name + a.lowerchar

        prev2Vowel = a.isVowel and prevVowel
        prev2Consonant = a.isConsonant and prevConsonant
        prevVowel = a.isVowel
        prevConsonant = a.isConsonant

    return name

def getLetter(needConsonant, needVowel):
    global alphabet

    done = False
    while(not done):
        a = alphabet[randint(0, 25)]
        if((needConsonant and a.isVowel) or (needVowel and a.isConsonant)):
            done = False
        else:
            done = True

    return a

yourName = makeName()
print(yourName)
