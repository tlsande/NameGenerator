import csv


class letter():
    def __init__(self, lowerChar, upperChar, isVowel, isConsonant):
        self.upperChar = upperChar
        self.lowerChar = lowerChar
        self.isVowel = isVowel
        self.isConsonant = isConsonant

def print2dArray(arr, n):
    for x in range(0, n):
        for y in range(0, n):
            print(arr[x][y], end='')
        print('\n')

def normalize(prob, n):
    newProb = prob

    for i in range(0, n):
        total = 0
        for j in range(0, n):
            total += prob[i][j]
        if(total > 0):
            for j in range(0, n):
                newProb[i][j] = prob[i][j] / total
        else:
            for j in range(0, n):
                newProb[i][j] = 1.0 / n
    return newProb


def main():
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

    # prob = [[0]*len(alphjabet)]*len(alphabet)
    prob = []
    # Name of file to read base matrix
    filename = 'base.csv'
    raceName = 'human'

    with open(filename, newline='') as csvfile:
        probReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in probReader:
            prob.append([])
            for num in row:
                prob[len(prob)-1].append(float(num))


    filename = raceName + ' names.csv'
    with open(filename, newline='') as csvfile:
        nameReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for names in nameReader:
            name = names[0]
            for i in range(0, len(name) - 1):
                letter1 = name[i]
                letter2 = name[i + 1]
                num1 = 0
                num2 = 0
                for i in range(0, len(alphabet)):
                    if(letter1 == alphabet[i].lowerChar or letter1 == alphabet[i].upperChar):
                        num1 = i
                    if(letter2 == alphabet[i].lowerChar or letter2 == alphabet[i].upperChar):
                        num2 = i
                prob[num1][num2] += 1

    prob = normalize(prob, len(alphabet))

    filename = raceName + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        probWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(alphabet)):
            probWriter.writerow(prob[i])
        # probWriter.writerows(prob)

if __name__ == "__main__":
    main()
