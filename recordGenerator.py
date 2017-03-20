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

import Record


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

cursor = db.cursor()

# create Record object
record = Record.Record()

# generate gender
# gender = record.generateGender()
# generate first name
# fName = record.generateFirstName(gender)
# generate surname
# lName = record.generateLastName()
# generate phone number
# phoneNum = record.generatePhoneNumber()

# does the same thing as the commented code above
record.generateRecord()

# debug code
print(record.firstName)
print(record.lastName)
print(record.age)
print(record.gender)
print(record.phoneNum)



#for digit in num:
        #print(digit, end='', flush=True)
