import random

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

class Record:

    # default constructor
    def __init__(self):
        self.gender = ''
        self.firstName = ''
        self.lastName = ''
        self.phoneNum = ''
        self.age = ''

    # generates complete record
    def generateRecord(self):
        self.gender = self.generateGender()
        self.firstName = self.generateFirstName(self.gender)
        self.lastName = self.generateLastName()
        self.phoneNum = self.generatePhoneNumber()
        self.age = self.generateAge()

    def generateGender(self):
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


    def generateAge(self):
        return random.randint(18, 100)


    def generatePhoneNumber(self):
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
                self.generateNumberSet(phoneNumber, 3)
                phoneNumber.append(' ')
            self.generateNumberSet(phoneNumber, 4)
        elif numType == 1:
            for i in range(2):
                self.generateNumberSet(phoneNumber, 3)
                phoneNumber.append('-')
            self.generateNumberSet(phoneNumber, 4)
        elif numType == 2:
            phoneNumber.append('(')
            self.generateNumberSet(phoneNumber, 3)
            phoneNumber.append(')')

            phoneNumber.append(' ')

            self.generateNumberSet(phoneNumber, 3)

            phoneNumber.append(' ')

            self.generateNumberSet(phoneNumber, 4)
        elif numType == 3:
            phoneNumber.append('(')
            self.generateNumberSet(phoneNumber, 3)
            phoneNumber.append(')')

            phoneNumber.append(' ')

            self.generateNumberSet(phoneNumber, 3)

            phoneNumber.append('-')

            self.generateNumberSet(phoneNumber, 4)
        elif numType == 4:
            for i in range(2):
                self.generateNumberSet(phoneNumber, 3)

                phoneNumber.append('.')

            self.generateNumberSet(phoneNumber, 4)

        elif numType == 5:
            phoneNumber.append('(')
            self.generateNumberSet(phoneNumber, 3)
            phoneNumber.append(')')

            phoneNumber.append(' ')

            self.generateNumberSet(phoneNumber, 3)

            phoneNumber.append('.')

            self.generateNumberSet(phoneNumber, 4)
        elif numType == 6:
            self.generateNumberSet(phoneNumber, 10)

        return phoneNumber


    def generateFirstName(self, gender):
        """
                randomly pulls a first name from a file depending on a
                randomly generated line number and the gender parameter passed to the function

                :return |string| a male or female first or last name:
            """

        if gender == 'M':
            # open male name file, generate random number, pull name at that line number, and return it properly capitalized
            return self.pullName('mFirst.txt').capitalize()
        else:
            # open female name file, generate random number, pull name at that line number, and return it properly capitalized
            return self.pullName('fFirst.txt').capitalize()

    def generateLastName(self):
        """
                randomly pulls a first name from a file depending on a
                randomly generated line number

                :return |string| surname:
            """
        return self.pullName('surnames.txt').capitalize()

    def generateNumberSet(self, numList, numDigits):
        """

            :param |list| numList -- list to have digits appended:
            :param |int| numDigits -- number of digits appended to numList:
            """
        for i in range(numDigits):
            numList.append(random.randint(0, 9))

    def pullName(self, filename):
        """

            :param filename filename of a name file:
            :return |string| a male or female name at idx index:
            """
        with open(filename) as namefile:
            names = []
            for name in namefile:
                names.append(name)
            idx = random.randint(0, MALE_LENGTH)
            # returns name at a particular index with the newline character stripped out
            return names[idx].strip('\n')

    def insertRecord(self, db, cursor):
        # insert record in db
        cursor.execute('''INSERT INTO real_fake_doors.person_info (
        first_name,
        last_name,
        gender,
        phone_num,
        age)
        VALUES(%s, %s, %s, %s, %s''', (self.firstName, self.lastName, self.gender, self.phoneNum, self.age))

        # commit change to db
        db.commit()

    def recordExists(self, cursor):
        # check db's duplicates table for phone num record
        # if exists in duplicates, increment counter for given record
        # if it doesn't exist in duplicates, insert it, set counter to 1

    def printRecord(self):
        print('First name: ')
        print(self.firstName)

        print('Last name: ')
        print(self.lastName)

        print('Age: ')
        print(self.age)

        print('Gender: ')
        print(self.gender)

        print('Phone number: ')
        for i in range(len(self.phoneNum)):
            print(self.phoneNum[i], end='', flush=True)

