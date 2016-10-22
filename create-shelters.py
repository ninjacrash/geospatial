#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 02:44:00 2016

@author: clesiemo3
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:54:22 2016

@author: clesiemo3
"""
import requests
import psycopg2
import sys
import random 
import string
import config
import csv

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

   
def db_start():
    con = None

    try:
        con = psycopg2.connect(database=config.DB_NAME,
                               user=config.DB_USER,
                               host=config.DB_HOST,
                               password=config.DB_PASS)
        return con
    except psycopg2.DatabaseError as e:

        if con:
            con.rollback()

        print('Error %s' % e)
        sys.exit(1)


def db_write(con, record):
    try:
        cur = con.cursor()
        query = 'insert into public.shelter (org_id, capacity, phone,' \
                'street_address, city, zip_code, county, state, country,' \
                'shelter_name, latitude, longitude, gender_restriction)' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        cur.execute(query, record)
        con.commit()
        cur.close()


    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print('Error %s' % e)

if __name__ == '__main__':
    
    with open('towns.csv', 'r') as f:
        reader = csv.reader(f)
        towns = list(reader)

    #reason = ['drug_abuse','domestic_abuse','medical_bills','student_loan']
    gender = [None,None,None,None,'m','m','m','f','f','f','x','q']
    #edu = ['ged','high_school','associates','bachelors','masters','phd']
    tf = [True, False]
    #dep = [0,0,0,1,2,3,4]

    #eth = ['white','black','asian','pacific_islander','prefer_not_to_disclose']
    con = db_start()
    for i in range(0,len(towns)):
        record = (random.choice([1,3]),random.randint(1,100),'555-555-5555',
                  randomword(10),towns[i][0],random.randint(10000,80000),randomword(7),randomword(2),randomword(3),towns[i][0]+" shelter",
                    towns[i][1],towns[i][2],random.choice(gender))
        #print(record)
        db_write(con,record)
    