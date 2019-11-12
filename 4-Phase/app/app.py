from datetime import datetime, date
import getpass
import re
import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

'''
cur.execute('select * from STARTUP')
print(cur.fetchall())
'''

# Functions to check the field_lists

def check_degree(d):
    degrees = {
        "btech" : "BTech",
        "mtech" : "MTech",
        "phd" : "PhD",
        "bsc" : "BSc",
        "ms" : "MS",
        "mphil" : "MPhil",
        "msc" : "MSc", 
        "bba" : "BBA",
        "mba" : "MBA", 
        "mbbs" : "MBBS",
        "bpharma" : "BPharma" 
    }
    if d.lower() in degrees.keys():
        return degrees[d.lower()]
    else:
        return None


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

ANSI_TEXT_RED = "\033[1;31m"
ANSI_TEXT_BLACK = "\033[1;31m"
ANSI_TEXT_GREEN = "\033[1;32m"
ANSI_TEXT_YELLOW = "\033[1;33m"
ANSI_TEXT_BLUE = "\033[1;34m"
ANSI_TEXT_PURPLE = "\033[1;35m"
ANSI_TEXT_CYAN = "\033[1;36m"
ANSI_TEXT_WHITE = "\033[1;37m"
ANSI_TEXT_RESET = "\033[1;0m"
command_list = []
command_list.append("Show")
command_list.append("Insert")
command_list.append("Update")
command_list.append("Delete")
command_list.append("Generate Report")
command_list.append("")
command_list.append("")
command_list.append("Quit")
show_list = []
show_list.append("Employee")
show_list.append("Resource")
show_list.append("Industry")
show_list.append("Location")
show_list.append("Investor")
show_list.append("Startup")
show_list.append("Project")
show_list.append("Director")
show_list.append("Director_Education")
show_list.append("Investor_Education")
show_list.append("Invests")
show_list.append("Based_in")
show_list.append("Startup Founders")
insert_list = []
insert_list.append("Investor")
insert_list.append("Startup")
insert_list.append("Employee")
insert_list.append("Industry")
update_list = []
update_list.append("Salary of employee")
update_list.append("Networth of employee")
delete_list = []
delete_list.append("Investor")
delete_list.append("Employee")
delete_list.append("Director")
report_list = []
report_list.append("Startup per Location")
report_list.append("Startup per Industry")


# Render Tables

def render_table(data):
    data_dict = {}
    for i in range(len(data)):
        for j in data[i]:
            if j not in data_dict.keys():
                data_dict[j] = [data[i][j]]
            else:
                data_dict[j].append(data[i][j])

    print(tabulate(data_dict, headers="keys", tablefmt="grid"))

    return


##################################################################################
############################    DISPLAY FUNCTIONS    #############################
##################################################################################
def allshow_employee():
    '''
    Function to show employee
    '''
    print("ME cvalle\n")
    try:
        query = "SELECT * FROM EMPLOYEE"
        cur.execute(query)
        render_table(cur.fetchall())
        # print(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)

    print(ANSI_TEXT_RESET)


def allshow_resource():
    '''
    Function to show resource
    '''
    try:
        query = "SELECT * FROM RESOURCE"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_industry():
    '''
    Function to show industry
    '''
    try:
        query = "SELECT * FROM INDUSTRY"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_location():
    '''
    Function to show location
    '''
    try:
        query = "SELECT * FROM LOCATION"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_investor():
    '''
    Function to show investor
    '''
    try:
        query = "SELECT * FROM INVESTOR"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_startup():
    '''
    Function to show all the startups
    '''
    try:
        query = "SELECT * FROM STARTUP"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_project():
    '''
    Function to show project
    '''
    try:
        query = "SELECT * FROM PROJECT"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_director():
    '''
    Function to show director
    '''
    try:
        query = "SELECT * FROM DIRECTOR"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_director_education():
    '''
    Function to show directors education
    '''
    try:
        query = "SELECT * FROM DIRECTOR_EDUCATION"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_investor_education():
    '''
    Function to show directors education
    '''
    try:
        query = "SELECT * FROM INVESTOR_EDUCATION"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_invests():
    '''
    Function to show directors education
    '''
    try:
        query = "SELECT * FROM INVESTS"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_based_in():
    '''
    Function to show directors education
    '''
    try:
        query = "SELECT * FROM BASED_IN"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


def allshow_startup_founders():
    '''
    Function to show directors education
    '''
    try:
        query = "SELECT * FROM STARTUP_FOUNDERS"
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)


##############################################################################
############################    INSERT FUNCTIONS    ##########################
##############################################################################
def insert_investor():
    '''
        Function to insert investors into the table
    '''

    inv_id = input("Enter Id: ")
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

    [fname, lname] = str(input("Enter Name (Fname, Lname): ")).split()

    lid = input("Enter Location Id (Pincode): ")
    while re.findall(r"[0-9]+", lid) == [] or re.findall(r"[0-9]+", lid)[0] != lid:
        print("LID not integer")
        lid = input("Enter Location Id: ")





    print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into INVESTOR(InvestorId,DOB,Sex,FirstName,LastName,LocationId) values(%d,'%s','%s','%s','%s',%d)" % (
        int(inv_id), dob, sex, fname, lname, int(lid))

    vart=0
    try:
        cur.execute(query)
    except Exception as e:
        con.commit()
        con.rollback()
        vart=1
        print("ERROR >>", e)

    if (vart==0):
        tr = 0
        while tr==0:
            print("Enter Invertor's Education\n")
            deg=input("Enter Degree: ")
            branch = input ("Enter Branch: ")
            invalid=1
            while (invalid):
                year = input ("Enter Year of Completion: ")
                while re.findall(r"[0-9]+", year) == [] or re.findall(r"[0-9]+", year)[0] != year:
                    print("year not integer")
                    year = input ("Enter Year of Completion: ")
                by=int(dob[:4]) 
                if int(year)-by<=5:
                    print ("Too young for a degree")
                else :
                    invalid=0
            query = "insert into INVESTOR_EDUCATION(InvestorID,Degree,Branch,Year) values(%d,'%s','%s','%d')" % (
                int(inv_id), deg,branch ,int(year))
            try:
                cur.execute(query)
            except Exception as e:
                con.commit()
                con.rollback()
                print("ERROR >>", e)
            k=input("are there more Educational Qualifications (Y/N)? ")
            if k[0]=='n' or k[0]=='N':
                tr=1

    print(ANSI_TEXT_RESET)

    return


def insert_startup():
    '''
        Function to insert startup into the table
    '''

    st_id = input("Enter Id: ")
    while re.findall(r"[0-9]+", st_id) == [] or re.findall(r"[0-9]+", st_id)[0] != st_id:
        print("ID not integer")
        st_id = input("Enter Id: ")

    st_name = str(input("Enter Startup Name: "))

    noE = input("Enter Number of Employees: ")
    while re.findall(r"[0-9]+", noE) == [] or re.findall(r"[0-9]+", noE)[0] != noE:
        print("Number of Employees not integer")
        noE = input("Enter Number of Employees: ")

    networth = input("Enter Networth: ")
    while re.findall(r"[0-9]+", networth) == [] or re.findall(r"[0-9]+", networth)[0] != networth:
        print("Networth not integer")
        networth = input("Enter Networth: ")

    lid = input("Enter Location Id (Pincode): ")
    while re.findall(r"[0-9]+", lid) == [] or re.findall(r"[0-9]+", lid)[0] != lid:
        print("LID not integer")
        lid = input("Enter Location Id: ")

    print(st_id, st_name, noE, networth, lid)

    query = "insert into STARTUP(StartupId,StartupName,NoofEmployees,Networth,LocationId) values(%d,'%s',%d, %d, %d)" % (
        int(st_id), st_name, int(noE), int(networth), int(lid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)

    return


def insert_employee():
    '''
        Function to insert employees into the table
    '''

    emp_id = input("Enter Id: ")
    while re.findall(r"[0-9]+", emp_id) == [] or re.findall(r"[0-9]+", emp_id)[0] != emp_id:
        print("ID not integer")
        emp_id = input("Enter Id: ")

    name = str(input("Enter Name: "))

    dept = str(input("Enter Department: "))

    salary = input("Enter Salary: ")
    while re.findall(r"[0-9]+", salary) == [] or re.findall(r"[0-9]+", salary)[0] != salary:
        print("Salary not integer")
        salary = input("Enter Salary: ")

    sex = str(input("Enter Sex (Male/Female): "))
    while check_sex(sex) == False:
        print("INVALID SEX")
        sex = str(input("Enter Sex: "))

    rid = input("Enter Location Id (Pincode): ")
    while re.findall(r"[0-9]+", rid) == [] or re.findall(r"[0-9]+", rid)[0] != rid:
        print("LID not integer")
        rid = input("Enter Location Id: ")

   # print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into EMPLOYEE(EmployeeID,EmployeeName,EmployeeDept,EmployeeSalary,EmployeeSex,ResourceID) values(%d,'%s','%s',%d,'%s',%d)" % (
        int(emp_id), name, dept, int(salary), sex, int(rid))

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)

    return


def insert_industry():
    '''
        Function to insert industries into the table
    '''

    ind_id = input("Enter Id: ")
    while re.findall(r"[0-9]+", ind_id) == [] or re.findall(r"[0-9]+", ind_id)[0] != ind_id:
        print("ID not integer")
        ind_id = input("Enter Id: ")

    name = str(input("Enter Name: "))

    type = str(input("Enter Industry Type: "))

   # print(inv_id, dob, sex, fname, lname, lid)

    query = "insert into INDUSTRY(IndustryID,IndustryName,IndustryType) values(%d,'%s','%s')" % (
        int(ind_id), name, type)

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)

    return

###############################################################################
############################    UPDATE FUNCTIONS    ###########################
###############################################################################


def update_employee_salary():
    '''
    Function to update the salary of an employee 
    '''
    emp_id = input("Enter Id of the employee whose salary is to updated: ")
    while re.findall(r"[0-9]+", emp_id) == [] or re.findall(r"[0-9]+", emp_id)[0] != emp_id:
        print("ID not integer")
        emp_id = input("Enter Id: ")

    salary = input("Enter new Salary: ")
    while re.findall(r"[0-9]+", salary) == [] or re.findall(r"[0-9]+", salary)[0] != salary:
        print("Salary not integer")
        salary = input("Enter Salary: ")

    try:
        query = "update EMPLOYEE set EmployeeSalary=%d where EmployeeId=%d" % (
            int(salary), int(emp_id))
        cur.execute(query)
        con.commit()
        print("Updated " + str(cur.rowcount) + " row(s) successfully")
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)

    return


def update_startup_networth():
    '''
    Function to update the networth of an startup
    '''
    st_id = input("Enter Id of the startup whose networth is to updated: ")
    while re.findall(r"[0-9]+", st_id) == [] or re.findall(r"[0-9]+", st_id)[0] != st_id:
        print("ID not integer")
        st_id = input("Enter Id: ")
    networth = input("Enter new networth: ")
    while re.findall(r"[0-9]+", networth) == [] or re.findall(r"[0-9]+", networth)[0] != networth:
        print("networth not integer")
        networth = input("Enter networth: ")

    try:
        query = "UPDATE STARTUP set Networth=%d where StartupID=%d" % (
            int(networth), int(st_id))
        cur.execute(query)
        con.commit()
        print("Updated " + str(cur.rowcount) + " row(s) successfully")
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)
    return

###############################################################################
############################    DELETE FUNCTIONS    ###########################
###############################################################################


def delete_investor():
    '''
    Function to delete the associated investor
    '''
    investor_id = input("Enter the investorID of the investor to delete: ")
    while re.findall(r"[0-9]+", investor_id) == [] or re.findall(r"[0-9]+", investor_id)[0] != investor_id:
        print("ID not integer")
        investor_id = input("Enter Id: ")
    try:
        query = "DELETE FROM INVESTOR WHERE InvestorID=%d" % (int(investor_id))
        cur.execute(query)
        con.commit()
        print("Deleted " + str(cur.rowcount) + " row(s) successfully")
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)
    return


def delete_employee():
    '''
    Function to delete the associated employee
    '''
    employee_id = input("Enter the employeeID of the employee to delete: ")
    while re.findall(r"[0-9]+", employee_id) == [] or re.findall(r"[0-9]+", employee_id)[0] != employee_id:
        print("ID not integer")
        employee_id = input("Enter Id: ")
    try:
        query = "DELETE FROM EMPLOYEE WHERE EmployeeID=%d" % (int(employee_id))
        cur.execute(query)
        con.commit()
        print("Deleted " + str(cur.rowcount) + " row(s) successfully")
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)
    return


def delete_director():
    '''
    Function to delete the associated investor
    '''
    startup_id = input("Enter the startupID of the director to delete: ")
    while re.findall(r"[0-9]+", startup_id) == [] or re.findall(r"[0-9]+", startup_id)[0] != startup_id:
        print("ID not integer")
        startup_id = input("Enter Id: ")
    name = input("Enter name of director to delete: ")
    try:
        query = "DELETE FROM DIRECTOR WHERE StartupID=%d AND Name='%s'" % (
            int(startup_id), str(name))
        cur.execute(query)
        con.commit()
        print("Deleted " + str(cur.rowcount) + " row(s) successfully")
    except Exception as e:
        con.rollback()
        print("ERROR >>", e)
    print(ANSI_TEXT_RESET)
    return


##################################################################################
############################    REPORT FUNCTION       ############################
##################################################################################

def max_startup_per_location():
    '''
    Function to find the location with the maximum number of startups and the number of startups
    '''
    query = 'select c as "Number of Startups", LocationID  from (select count(*) as c,LocationID from BASED_IN group by LocationID) as x where x.c = (select max(c)  from (select count(*) as c,LocationID from BASED_IN group by LocationID ) as y) group by LocationID;'
    try:
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("Error >> ", e)
    print(ANSI_TEXT_RESET)

    return


def max_startup_per_industry():
    '''
    Function to find the location with the maximum number of startups and the number of startups
    '''
    query = 'select c as "Number of Startups", x.IndustryID, IndustryName from (select count(StartupID) as c, IndustryID from INVESTS group by IndustryID) as x, INDUSTRY i where x.c = (select max(c) from (select count(StartupID) as c, IndustryID i from INVESTS group by IndustryID) as x) and i.IndustryID = x.IndustryID group by IndustryID ;'
    try:
        cur.execute(query)
        render_table(cur.fetchall())
    except Exception as e:
        con.rollback()
        print("Error >> ", e)
    print(ANSI_TEXT_RESET)

    return

def age_of_investor():
    '''
    Function to calculate the age of the investor
    '''
    inv_id = input("Enter the InvestorID of the director to delete: ")
    while re.findall(r"[0-9]+", inv_id) == [] or re.findall(r"[0-9]+", inv_id)[0] != inv_id:
        print("ID not integer")
        inv_id = input("Enter Id: ")

    query = "select DOB from INVESTOR where InvestorID = %d" % (int(inv_id))

    try:
        cur.execute(query)
        dob = cur.fetchone()[0]

        today = date.today()
        years = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            years -= 1

        print("The age of the investor is: ", years)
        return years 

    except Exception as e:
        con.rollback()
        print("Error >> ", e)
        


list_of_functions = [[allshow_employee, allshow_resource, allshow_industry, allshow_location, allshow_investor, allshow_startup, allshow_project, allshow_director, allshow_director_education, allshow_investor_education, allshow_invests, allshow_based_in,
                      allshow_startup_founders], [insert_investor, insert_startup, insert_employee, insert_industry], [update_employee_salary, update_startup_networth], [delete_investor, delete_employee, delete_director], [max_startup_per_location, max_startup_per_industry]]


##################################################################################
############################    MAIN FUNCTION       ##############################
##################################################################################
def execute_command(a):
    ''' 
    Function that redirect query to corresponding function 
    '''
    if a == 0:
        print(ANSI_TEXT_YELLOW)
        for i in range(len(show_list)):
            print(i, show_list[i])
        b = int(input("Enter an option to select: "))
        gp = list_of_functions[a][b]()

    elif a == 1:
        print(ANSI_TEXT_BLUE)
        for i in range(len(insert_list)):
            print(i, insert_list[i])
        b = int(input("Enter an option to select: "))
        gp = list_of_functions[a][b]()

    elif a == 2:
        print(ANSI_TEXT_GREEN)
        for i in range(len(update_list)):
            print(i, update_list[i])
        b = int(input("Enter an option to select: "))
        gp = list_of_functions[a][b]()

    elif a == 3:
        print(ANSI_TEXT_RED)
        for i in range(len(delete_list)):
            print(i, delete_list[i])
        b = int(input("Enter an option to select: "))
        gp = list_of_functions[a][b]()
    elif a == 4:
        print(ANSI_TEXT_CYAN)
        for i in range(len(report_list)):
            print(i, report_list[i])
        b = int(input("Enter an option to select: "))
        gp = list_of_functions[a][b]()

    print(ANSI_TEXT_RESET)
    return


tmp = sp.call('clear', shell=True)
logged = 0
while (logged == 0):
    try:
        logged = 1
        username = str(input("Enter user: "))
        password = str(getpass.getpass())
        con = pymysql.connect('localhost', username, password,
                              'incubator', cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        logged = 0
        print("ERROR>>>", e)

cur = con.cursor()
while True:
    print("Select an option")
    for h in range(len(command_list)):
        print(h, command_list[h])
    try:
        g = int(input("Enter the key: "))
        # allshow_employee()
        if (g == 7):
            exit()
        else:
            execute_command(g)
    except Exception as e:
        print("ERROR>>>", e)
    # update_networth()
    #cur.execute('select * from INVESTOR')

render_table(cur.fetchall())

