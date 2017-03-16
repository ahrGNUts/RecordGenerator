# python 3.4
# male first name list was pulled from: http://scrapmaker.com/view/names/male-names.txt
# female first name list was pulled from: http://deron.meranda.us/data/census-dist-female-first.txt
# I also edited the male and female first name lists
# surname list for this project was pulled from: https://github.com/enorvelle/NameDatabases
# TODO: generate random records, put in database
# TODO: implement a 'no duplication' search function that will make sure no duplicate entries are created


import random
import sql
import MySQLdb
import sys

# db connection stuff
try:
    db = MySQLdb.connect(
        host = 'localhost',
        user = 'py-record',
        passwd = '',
        db = 'real_fake_doors'
    )
except Exception as e:
    sys.exit('Database not detected')

# "constants" for number of elements in a file
MALE_LENGTH = 0
try:
    with open('mFirst.txt') as f:
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
    with open('surnames.txt') as f:
        for line in f:
            SURNAME_LENGTH += 1
except IOError:
    print("Surname name file not found.")


def pullName(filename):
    """

    :param filename filename of a name file:
    :return |string| a male or female name at idx index:
    """
    with open(filename) as namefile:
        names = []
        for name in namefile:
            names.append(name)
        idx = random.randint(0, MALE_LENGTH)
        return names[idx]

def generateFirstName(gender):
    """
        randomly pulls a first name from a file depending on a
        randomly generated line number and the gender parameter passed to the function

        :return |string| a male or female first or last name:
    """

    if gender == 'M':
        # open male name file, generate random number, pull name at that line number
        return pullName('mFirst.txt')
    else:
        # open female name file, generate random number, pull name at that line number
        return pullName('fFirst.txt')


def generateLastName():
    """
        randomly pulls a first name from a file depending on a
        randomly generated line number

        :return |string| surname:
    """
    return pullName('surnames.txt')


def generateGender():
    """
        randomly generates a gender and is used to determine a record's first name
        for simplicity, M/F is used

        :return |char| 'M' or 'F':
    """

    gender = random.randint(0, 1)

    if gender == 0:
        return 'M'
    else:
        return 'F'


def generateAge():

    return random.randint(18, 100)


def generateNumberSet(numList, numDigits):
    """

    :param |list| numList -- list to have digits appended:
    :param |int| numDigits -- number of digits appended to numList:
    """
    for i in range(numDigits):
        numList.append(random.randint(0, 9))

# check http://usrecordsearch.com/ssn.htm for information about SSN structure
# going to save this for a future version
# one thing at a time and all that.
def generateSSN():
    """
    generate a random SSN and check it against a list of previously generated numbers to ensure that it'
    not one that's already been assigned
    :return |list| social security number:
    """

    ssn = []

    generateNumberSet(ssn, 3)
    ssn.append('-')
    generateNumberSet(ssn, 2)
    ssn.append('-')
    generateNumberSet(ssn, 3)

    return ssn

def generatePhoneNumber():
    """
        phone number types:
        0: xxx xxx xxxx
        1: xxx-xxx-xxxx
        2: (xxx) xxx xxxx
        3: (xxx) xxx-xxxx
        4: xxx.xxx.xxxx
        5: (xxx) xxx.xxxx
        6: xxxxxxxxxx

    :return |list| phone number:
    """

    numType = random.randint(0, 6)
    phoneNumber = []

    if numType == 0:
        for i in range(2):
            generateNumberSet(phoneNumber, 3)
            phoneNumber.append(' ')
        generateNumberSet(phoneNumber, 4)
    elif numType == 1:
        for i in range(2):
            generateNumberSet(phoneNumber, 3)
            phoneNumber.append('-')
        generateNumberSet(phoneNumber, 4)
    elif numType == 2:
        phoneNumber.append('(')
        generateNumberSet(phoneNumber, 3)
        phoneNumber.append(')')

        phoneNumber.append(' ')

        generateNumberSet(phoneNumber, 3)

        phoneNumber.append(' ')

        generateNumberSet(phoneNumber, 4)
    elif numType == 3:
        phoneNumber.append('(')
        generateNumberSet(phoneNumber, 3)
        phoneNumber.append(')')

        phoneNumber.append(' ')

        generateNumberSet(phoneNumber, 3)

        phoneNumber.append('-')

        generateNumberSet(phoneNumber, 4)
    elif numType == 4:
        for i in range(2):
            generateNumberSet(phoneNumber, 3)

            phoneNumber.append('.')

        generateNumberSet(phoneNumber, 4)

    elif numType == 5:
        phoneNumber.append('(')
        generateNumberSet(phoneNumber, 3)
        phoneNumber.append(')')

        phoneNumber.append(' ')

        generateNumberSet(phoneNumber, 3)

        phoneNumber.append('.')

        generateNumberSet(phoneNumber, 4)
    elif numType == 6:
        generateNumberSet(phoneNumber, 10)

    return phoneNumber



# generate gender
gender = generateGender()
# generate first name
fName = generateFirstName(gender)
# generate surname
lName = generateLastName()
# generate phone number
phoneNum = generatePhoneNumber()




#for digit in num:
        #print(digit, end='', flush=True)
