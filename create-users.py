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
        query = 'insert into public.user (user_id,id_type,email,phone,reason,' \
                'password,gender,veteran,education,dependents,ethnicity,' \
                'homeless,employed)' \
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        cur.execute(query, record)
        con.commit()
        cur.close()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print('Error %s' % e)

if __name__ == '__main__':
    with open('emails.txt') as f:
        emails = f.readlines()
    reason = ['drug_abuse','domestic_abuse','medical_bills','student_loan']
    gender = ['m','m','m','f','f','f','x','q']
    edu = ['ged','high_school','associates','bachelors','masters','phd']
    tf = [True, False]
    dep = [0,0,0,1,2,3,4]
    eth = ['white','black','asian','pacific_islander','prefer_not_to_disclose']
    con = db_start()
    for email in emails:
        email = email.rstrip('\n')
        record = (email,'email',email,None,random.choice(reason),
                  randomword(10),random.choice(gender),random.choice(tf),
                  random.choice(edu),random.choice(dep),random.choice(eth),
                  random.choice(tf),random.choice(tf))
        #print(record)
        db_write(con,record)
    