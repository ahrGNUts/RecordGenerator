# python 3.4
# male first name list was pulled from: http://scrapmaker.com/view/names/male-names.txt
# female first name list was pulled from: http://deron.meranda.us/data/census-dist-female-first.txt
# I also edited the male and female first name lists
# surname list for this project was pulled from: https://github.com/enorvelle/NameDatabases
# TODO: pull names from male and female first name lists
import random

# "constants" for number of lines in a file
MALE_LENGTH = 0
try:
    with open('fFirst.txt') as f:
        for line in f:
            MALE_LENGTH += 1
except IOError:
    print("Male name file not found.")

FEMALE_LENGTH = 0
try:
    with open('fFirst.txt') as f:
        for line in f:
            FEMALE_LENGTH += 1
except IOError:
    print("Female name file not found.")

SURNAME_LENGTH = 0
try:
    with open('fFirst.txt') as f:
        for line in f:
            SURNAME_LENGTH += 1
except IOError:
    print("Surname name file not found.")


def generateFirstName(gender):
    """
        randomly pulls a first name from a file depending on a
        randomly generated line number and the gender parameter passed to the function

        :return :
    """

    if gender == 'M':
        # open male name file, generate random number, pull name at that line number
        with open('mFirst.txt') as namefile:
            names = []
            for name in namefile:
                names.append(name)
            idx = random.randint(0, MALE_LENGTH)
            return names[idx]
    else:
        # open female name file, generate random number, pull name at that line number
        with open('fFirst.txt') as namefile:
            names = []
            for name in namefile:
                names.append(name)
            idx = random.randint(0, FEMALE_LENGTH)
            return names[idx]


def generateLastName():
    """
        randomly pulls a first name from a file depending on a
        randomly generated line number

        :return:
    """


def generateGender():
    """
        randomly generates a gender and is used to determine a record's first name
        for simplicity, M/F is used


        :return character 'M' or 'F':
    """

    gender = random.randint(0, 1)

    if gender == 0:
        return 'M'
    else:
        return 'F'


def generateNumber():
    """
        phone number types:
        0: xxx xxx xxxx
        1: xxx-xxx-xxxx
        2: (xxx) xxx xxxx
        3: (xxx) xxx-xxxx
        4: xxx.xxx.xxxx
        5: (xxx) xxx.xxxx
        6: xxxxxxxxxx

    :return list phone number:
    """

    numType = random.randint(0, 6)
    number = []
    if numType == 0:
        for i in range(2):
            for k in range(3):
                number.append(random.randint(0, 9))
            number.append(' ')
        for i in range(4):
            number.append((random.randint(0, 9)))
    elif numType == 1:
        for i in range(2):
            for k in range(3):
                number.append(random.randint(0, 9))
            number.append('-')
        for i in range(4):
            number.append((random.randint(0, 9)))
    elif numType == 2:
        number.append('(')
        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(')')
        number.append(' ')

        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(' ')

        for i in range(4):
            number.append(random.randint(0, 9))
    elif numType == 3:
        number.append('(')
        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(')')
        number.append(' ')

        for i in range(3):
            number.append(random.randint(0, 9))

        number.append('-')

        for i in range(4):
            number.append(random.randint(0, 9))
    elif numType == 4:
        for i in range(2):
            for k in range(3):
                number.append(random.randint(0, 9))
            number.append('.')
        for i in range(4):
            number.append(random.randint(0, 9))
    elif numType == 5:
        number.append('(')

        for i in range(3):
            number.append(random.randint(0, 9))

        number.append(')')
        number.append(' ')

        for i in range(3):
            number.append(random.randint(0, 9))

        number.append('.')

        for i in range(4):
            number.append(random.randint(0, 9))
    elif numType == 6:
        for i in range(10):
            number.append(random.randint(0, 9))

    return number

    #print(number)
    """
    for digit in number:
        print(digit, end='', flush=True)
    """


generateNumber()
