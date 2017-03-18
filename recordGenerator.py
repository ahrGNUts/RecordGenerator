# python 3.4
# male first name list was pulled from: http://scrapmaker.com/view/names/male-names.txt
# female first name list was pulled from: http://deron.meranda.us/data/census-dist-female-first.txt
# I also edited the male and female first name lists
# surname list for this project was pulled from: https://github.com/enorvelle/NameDatabases
# TODO: generate random records, put in database
# TODO: implement a 'no duplication' search function that will make sure no duplicate entries are created


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

# create empty Record object
record = Record.Record()

# populate each field of
record.generateRecord()

# debug code; prints generated record
# record.printRecord()

