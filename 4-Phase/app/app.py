import pymysql
import pymysql.cursors
import getpass
import re
from datetime import datetime

username = str(input())
password = str(getpass.getpass())
con = pymysql.connect('localhost', username, password, 'incubator', cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()

cur.execute('select * from STARTUP')
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

    st_id = input("Enter Id: " )
    while re.findall(r"[0-9]+", st_id) == [] or re.findall(r"[0-9]+", st_id)[0] != st_id:
        print("ID not integer")
        st_id = input("Enter Id: ")

    st_name = str(input("Enter Startup Name: "))

    noE = input("Enter Number of Employees: ")
    while  re.findall(r"[0-9]+", noE) == [] or re.findall(r"[0-9]+", noE)[0] != noE:
        print("Number of Employees not integer")
        noE = input("Enter Number of Employees: ")

    networth = input("Enter Networth: ")
    while  re.findall(r"[0-9]+", networth) == [] or re.findall(r"[0-9]+", networth)[0] != networth:
        print("Networth not integer")
        networth = input("Enter Networth: ")

    lid = input("Enter Location Id (Pincode): ")
    while  re.findall(r"[0-9]+", lid) == [] or re.findall(r"[0-9]+", lid)[0] != lid:
        print("LID not integer")
        lid = input("Enter Location Id: ")


    print(st_id, st_name, noE, networth, lid)

    query = "insert into STARTUP(StartupId,StartupName,NoofEmployees,Networth,LocationId) values(%d,'%s',%d, %d, %d)" % (int(st_id), st_name, int(noE), int(networth), int(lid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    return

def insert_employee():
    '''
        Function to insert employees into the table
    '''

    emp_id = input("Enter Id: " )
    while re.findall(r"[0-9]+", emp_id) == [] or re.findall(r"[0-9]+", emp_id)[0] != emp_id:
        print("ID not integer")
        emp_id = input("Enter Id: ")

    name = str(input("Enter Name: "))
    
    dept = str(input( "Enter Department: "))


    salary = input("Enter Salary: ")
    while  re.findall(r"[0-9]+", salary) == [] or re.findall(r"[0-9]+", salary)[0] != salary:
        print("Salary not integer")
        salary = input("Enter Salary: ")

    sex = str(input("Enter Sex (Male/Female): "))
    while check_sex(sex) == False:
        print("INVALID SEX")
        sex = str(input("Enter Sex: "))

    rid = input("Enter Location Id (Pincode): ")
    while  re.findall(r"[0-9]+", rid) == [] or re.findall(r"[0-9]+", rid)[0] != rid:
        print("LID not integer")
        rid = input("Enter Location Id: ")


   # print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into EMPLOYEE(EmployeeID,EmployeeName,EmployeeDept,EmployeeSalary,EmployeeSex,ResourceID) values(%d,'%s','%s',%d,'%s',%d)" % (int(emp_id), name, dept, int(salary), sex, int(rid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    return

def insert_industry():
    '''
        Function to insert industries into the table
    '''

    ind_id = input("Enter Id: " )
    while re.findall(r"[0-9]+", ind_id) == [] or re.findall(r"[0-9]+", ind_id)[0] != ind_id:
        print("ID not integer")
        ind_id = input("Enter Id: ")

    name = str(input("Enter Name: "))
    
    type = str(input( "Enter Industry Type: "))

   # print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into INDUSTRY(IndustryID,IndustryName,IndustryType) values(%d,'%s','%s')" % (int(ind_id), name, type)

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    return


insert_industry()
cur.execute('select * from INDUSTRY')

print(cur.fetchall())
