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

    # debug method
    def setRecord(self, gender, first, last, phone, age):
        self.gender = gender
        self.firstName = first
        self.lastName = last
        self.phoneNum = phone
        self.age = age

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
                generates a phone number in the format of:
                (xxx) xxx-xxxx
                
                stripped down from previous state for less work while querying db and looking for duplicates

            :return |string| phone number:
            """

        phoneNumber = []

        phoneNumber.append('(')
        self.generateNumberSet(phoneNumber, 3)
        phoneNumber.append(')')

        phoneNumber.append(' ')

        self.generateNumberSet(phoneNumber, 3)
        phoneNumber.append('-')
        self.generateNumberSet(phoneNumber, 4)

        tmp = ''.join(map(str, phoneNumber))

        return tmp


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
        updateType = [0]
        if self.recordExists(cursor, updateType):
            self.updateDuplicateRecord(db, cursor, updateType)
        else:
            cursor.execute('''INSERT INTO person_info (
            first_name,
            last_name,
            gender,
            phone_num,
            age
            )
            VALUES(%s, %s, %s, %s, %s)''', (self.firstName, self.lastName, self.gender, self.phoneNum, self.age))

            # commit change to db
            db.commit()

    def updateDuplicateRecord(self, db, cursor, updateType):
        # update counter value in duplicates
        if updateType[0] == 1:
            cursor.execute(''' UPDATE duplicates SET num_duplicates=num_duplicates+1
                                WHERE phone_num LIKE %s''', self.phoneNum)
        elif updateType[0] == 2:
            # insert new record into 'duplicates' and 'duplicate_details' tables
            cursor.execute('''INSERT INTO duplicates (
                        phone_num,
                        num_duplicates
                        )
                        VALUES(%s, %s)''', (self.phoneNum, 0))
        else:
            print("Something has gone horribly wrong...")

        # add details of new duplicate instance into table
        cursor.execute('''INSERT INTO duplicate_details (
                    first_name,
                    last_name,
                    gender,
                    phone_num,
                    age
                    ) VALUES(%s, %s, %s, %s, %s)''',
                       (self.firstName, self.lastName, self.gender, self.phoneNum, self.age))

        db.commit()


    def recordExists(self, cursor, updateType):
        # check db's duplicates table for phone num record
        # if exists in duplicates, increment counter for given record, add record info to duplicate_details
        # if it doesn't exist in duplicates, search person_info
        # if found in person_info:
        """
            1. insert phone num into table 'duplicates'.phone_num
            2. set duplicates.num_duplicates to 1
            3. add record info to table 'duplicate_details'
        """
        #num = ''.join(str(n) for n in self.phoneNum)

        command = "SELECT * FROM duplicates WHERE phone_num LIKE '{0}'".format(self.phoneNum)

        duplicateExists = cursor.execute(command)

        if duplicateExists:
            updateType = [1]
            return True
        else:
            command = "SELECT * FROM person_info WHERE phone_num LIKE '{0}'".format(self.phoneNum) # chokes here; expected str instance, bytes found
            recExists = cursor.execute(command)

            if recExists:
                updateType = [2]
                return True
            else:
                return False


    def displayRecord(self):
        print('\nFirst name: ')
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

        print('\n')

