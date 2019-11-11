import pymysql
import pymysql.cursors
import getpass
import re
from datetime import datetime

username = str(input())
password = str(getpass.getpass())
con = pymysql.connect('localhost', username, password, 'incubator', cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()

cur.execute('select * from INVESTOR')
print(cur.fetchall())


# Functions to check the field_lists
def check_sex(c):
    return(c in ['Male', 'Female'])

def parse_date(d):
    try:
        parsed_date = datetime.strptime(d, '%Y-%m-%d').strftime('%Y-%m-%d')
        return parsed_date
    except:
        return None

if parse_date('1993-02-23') is None:
    print("WRONG INPUT")
else:
    print(parse_date('1993-02-21'))


# Insert functions
def insert_investor():
    '''
        Function to insert investors into the table
    '''
    inv_id = input("Enter Id: " )
    while re.findall(r"[0-9]+", inv_id) == [] or re.findall(r"[0-9]+", inv_id)[0] != inv_id:
        print("ID not integer")
        inv_id = input("Enter Id: ")

    dob = str(input("Enter Date YYYY-MM-DD:"))
    while parse_date(dob) is None:
        print("WRONG DATE")
        dob = str(input("Enter Date YYYY-MM-DD: "))

    sex = str(input("Enter Sex (Male/Female): "))
    while check_sex(sex) == False:
        print("INVALID SEX")
        sex = str(input("Enter Sex: "))

    [fname,lname] = str(input("Enter Name (Fname, Lname): ")).split()

    lid = input("Enter Location Id (Pincode): ")
    while  re.findall(r"[0-9]+", lid) == [] or re.findall(r"[0-9]+", lid)[0] != lid:
        print("LID not integer")
        lid = input("Enter Location Id: ")


    print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into INVESTOR(InvestorId,DOB,Sex,FirstName,LastName,LocationId) values(%d,'%s','%s','%s','%s',%d)" % (int(inv_id), dob, sex, fname, lname, int(lid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    return


def insert_startup():
    '''
        Function to insert startup into the table
    '''
    inv_id = input("Enter Id: " )
    while re.findall(r"[0-9]+", inv_id) == [] or re.findall(r"[0-9]+", inv_id)[0] != inv_id:
        print("ID not integer")
        inv_id = input("Enter Id: ")

    dob = str(input("Enter Date YYYY-MM-DD:"))
    while parse_date(dob) is None:
        print("WRONG DATE")
        dob = str(input("Enter Date YYYY-MM-DD: "))

    sex = str(input("Enter Sex (Male/Female): "))
    while check_sex(sex) == False:
        print("INVALID SEX")
        sex = str(input("Enter Sex: "))

    [fname,lname] = str(input("Enter Name (Fname, Lname): ")).split()

    lid = input("Enter Location Id (Pincode): ")
    while  re.findall(r"[0-9]+", lid) == [] or re.findall(r"[0-9]+", lid)[0] != lid:
        print("LID not integer")
        lid = input("Enter Location Id: ")


    print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into INVESTOR(InvestorId,DOB,Sex,FirstName,LastName,LocationId) values(%d,'%s','%s','%s','%s',%d)" % (int(inv_id), dob, sex, fname, lname, int(lid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    return


insert_investor()
cur.execute('select * from EMPLOYEE')

print(cur.fetchall())
