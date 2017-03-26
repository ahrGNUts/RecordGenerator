# python 3.4
# male first name list was pulled from: http://scrapmaker.com/view/names/male-names.txt
# female first name list was pulled from: http://deron.meranda.us/data/census-dist-female-first.txt
# I also edited the male and female first name lists
# surname list for this project was pulled from: https://github.com/enorvelle/NameDatabases
# TODO: generate random records, put in database
# TODO: implement a 'no duplication' search function that will make sure no duplicate entries are created


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

# create empty Record object
record = Record.Record()

while True:
    print("Functionality testing time!")
    print("1. Generate and display record")
    print("2. Insert new record into db")
    print("3. Create record, commit to db, create exact duplicate record, commit to db")
    print("4. Create record, commit to db, create record with duplicate phone num, commit to db")

    try:
        choice = int(input('Pick u a num w/ no period: '))
    except ValueError as e:
        print("Nah, you have to pick a number. Try it again.\n")

    if choice == 1:
        record.generateRecord()
        record.displayRecord()
    elif choice == 2:
        record.generateRecord()
        record.insertRecord(db, cursor)
    elif choice == 3:
        record.generateRecord()
        
# populate each field of record object
#record.generateRecord()

# debug code; prints generated record
# record.printRecord()

