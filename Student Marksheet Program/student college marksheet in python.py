import mysql.connector
import pandas as pd 
from os import system
db = mysql.connector.connect(host="localhost",user="root",passwd="1234")

cursor = db.cursor()
# cursor.execute("drop database if exists college")
cursor.execute("create database if not exists college ")
cursor.execute("use college")
cursor.execute("create table if not exists entries (rollno int AUTO_INCREMENT primary key, name varchar(255), course varchar(255),semester int,year int)")

def add():
    # roll  = 1
    # year = 23
    # rollnumber = f"{roll:04n}"
    # rollnumber = str(year)+str(rollnumber)
    # rollnumber = int(rollnumber)
    # print(rollnumber)
    name = input("Enter her/his name : ")
    course = "B.Tech. Computer science "
    semester = 1
    year = 1
    # rollnumber = 230001
    sql = "insert into entries(name,course,semester,year) value(%s,%s,%s,%s)"
    x = (name,course,semester,year)
    cursor.execute(sql,x)
    db.commit()

    cursor.execute("select rollno from entries order by rollno desc limit 1")
    rollno = cursor.fetchall()
    print("your roll number is : ",rollno[0][0])
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
# add()
# making a subject table that consiste of all the subjects of the student 
# make all once and run it once only (type of function)
def sujbects():
    s1 = (1,"Mathematics 1","Physics",'Basic Electonics','Caeg','Communicstion Skills',"Problem Solving Programming in C")
    s2 = ('Mathematics 2','Chemisty',"Civil Engineering","CAMD",'Human Values','Mechanical')
    s3 = ('Advanced Mathematics','Digital Electronics','Techanical Communication','Data Structure and Algorithm','Object Oriented Programming','Software Engineering')
    s4 = ('Discrete Mathematics','accounting communication','Microprocessors','Database Management System','Theory of Computation','Data Communication and Computer Networks')
    s5 = ('Information Theory & Coding ','Compiler Design','Operating System ','Computer Graphics & Multimedia','Wireless communication','Analysis of Algorithm')
    s6 = ('Digital Image Processing','Machine Learning',' Information Security System','Computer Architecture and Organization','Artificial Intelligence','Cloud Computing') 
    s7 = ('Internet of Things','Open Elective - I ')
    s8 = ('Big Data Analytics','Open Elective - II ')
    cursor.execute("create table if not exists subject(sno int primary key AUTO_INCREMENT,s1 varchar(255),s2 varchar(255),s3 varchar(255),s4 varchar(255),s5 varchar(255),s6 varchar(255))");
    # sqls1 = "insert into subject(sno,s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls1,s1)
    # db.commit()

    # sqls2 = "insert into subject(s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls2,s2)
    # db.commit()

    # sqls3 = "insert into subject(s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls3,s3)
    # db.commit()

    # sqls4 = "insert into subject(s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls4,s4)
    # db.commit()

    # sqls5 = "insert into subject(s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls5,s5)
    # db.commit()

    # sqls8 = "insert into subject(s1,s2) values(%s,%s)"
    # cursor.execute(sqls8,s8)
    # db.commit()

    # sqls7 = "insert into subject(s1,s2) values(%s,%s)"
    # cursor.execute(sqls7,s7)
    # db.commit()

    # sqls6 = "insert into subject(s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sqls6,s6)
    # db.commit()

def entermarks():
    cursor = db.cursor()
    cursor.execute("create table if not exists marks(rollno int,semester int ,typeofexam varchar(255), s1 int,s2 int,s3 int,s4 int,s5 int,s6 int)")
    while(1):
        rollno = int(input("enter the roll number : "))
        sql = "select rollno,name from entries where rollno = %s"
        roll = (rollno,)
        cursor.execute(sql,roll)
        name = cursor.fetchall()
        if name:
            # print(name)
            name = str(name[0][1])
            print(name)
            # print(type(name))
            break
        else :
            print("Record not found \nEnter again")

    while(1):
        semester = int(input("enter the semester : "))

        if semester == 1:
            break
        heylo = 1
        if semester > 1 and semester< 9:   
            sql1 = "select * from marks where rollno = %s and typeofexam =  'Midterm 1' and semester = %s"
            sql2 = "select * from marks where rollno = %s and typeofexam =  'Midterm 2' and semester = %s"
            sql3 = "select * from marks where rollno = %s and typeofexam =  'End semester examination' and semester = %s"
            x = (rollno,semester-1)
            cursor.execute(sql1,x)
            first =  cursor.fetchall()
            cursor.execute(sql2,x)
            second = cursor.fetchall()
            cursor.execute(sql3,x)
            third = cursor.fetchall()
            if (first and second and third):
                break
            else:
                if semester <=8 and semester > 1:
                    print("you havent entered marks for : ",semester-1," semester  \nEnter again")

    while(1):
        typeofexam  = int(input("Select The Type of Exam \n1. Midterm 1 \n2. Midterm 2 \n3. End semester examination \nenter a choice : "))
        if typeofexam == 1 or 2 or 3:
            if typeofexam == 1:
                typeofexam="Midterm 1"
            elif typeofexam == 2:
                typeofexam ="Midterm 2"
            elif typeofexam == 3:
                typeofexam ="End semester examination"
        break
    
    sql = "select * from subject where sno = %s"
    sem = (semester,)
    cursor.execute(sql,sem)
    subjects = cursor.fetchall()
    # print(subjects)
    print("for ",typeofexam,"enter the per subject marks : ") 
    while (1):
        print(subjects[0][1],end='')
        s1 = int(input( ": "))
        print(subjects[0][2],end='')
        s2 = int(input(" : "))
        if subjects[0][3]!=None:
            print(subjects[0][3],end='')
            s3 = int(input(" : "))
            print(subjects[0][4],end='')
            s4 = int(input(" : "))
            print(subjects[0][5],end='')
            s5 = int(input(" : "))
            print(subjects[0][6],end='')
            s6 = int(input(" : "))
        else :
            s3=s4=s5=s6=-1

        if s1>=-1 and s2>=-1 and s3>=-1 and s4>=-1 and s5>=-1 and s6 >=-1 and s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100 and s6 <=100:
            print(s1,s2,s3,s4,s5,s6)
            break
        else:
            print("enter the marks again they must be above '0' and under '100' ")
            
    # percentage = int((s1+s2+s3+s4+s5+s6)/6)
    # print(rollno,type(rollno))
    # print(name,type(name))
    # print(semester,type(semester))
    # print(typeofexam,type(typeofexam))
    # print(s1,type(s2))
    # print(s2,type(s2))
    # print(s3,type(s3))
    # print(s4,type(s4))
    # print(s5,type(s5))
    # print(s6,type(s6))
    # print(percentage,type(percentage))

    sql = "select * from marks where rollno = %s and semester = %s and typeofexam = %s"
    xx = (rollno,semester,typeofexam)
    cursor.execute(sql,xx)
    search = cursor.fetchall()
    if (search):
        choice = int(input("The record already exists \nDo you want to insert the row \nTo isert the row press(1) : "))
        if choice == 1:
            sql = "update marks set s1 = %s,s2 = %s,s3 = %s,s4 = %s,s5 = %s ,s6 = %s where rollno = %s and semester = %s and typeofexam = %s"
            xxx = (s1,s2,s3,s4,s5,s6,rollno,semester,typeofexam)
            cursor.execute(sql,xxx)
            db.commit()
            print("table editted")
        else:
            pass

    else:
        main = "insert into marks(rollno,semester,typeofexam,s1,s2,s3,s4,s5,s6) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        x = (rollno,semester,typeofexam,s1,s2,s3,s4,s5,s6)
        print(x)
        cursor.execute(main,x)
        db.commit()
        print("done")

# entermarks()

def show():
    while(1):
        rollno = int(input("enter the roll number : "))
        sql = "select rollno,name from entries where rollno = %s"
        roll = (rollno,)
        cursor.execute(sql,roll)
        name = cursor.fetchall()
        if name:
            break
        else :
            print("Record not found \nEnter again")

    semester = int(input("enter the semester : "))

    system('cls')
    print("<<----REPORT CARD---->>")
    # print(name)
    name = str(name[0][1])
    print(name,end='')
    print("\t\t",rollno)
    # print(type(name))


    flag = 0 
    while(semester != 0):  

        sql = "select s1,s2,s3,s4,s5,s6 from marks where rollno = %s and semester = %s"
        x = (rollno,semester)
        cursor.execute(sql,x)
        marks = cursor.fetchall()
        if marks:
            # for x in marks:
            #     print(x)
            pass
                
        else:
            print("Marks not entered") 
            break
        subs = "select s1,s2,s3,s4,s5,s6 from subject where sno = %s"
        x = (semester,)
        cursor.execute(subs,x)
        subjects = cursor.fetchall()
        # print(subjects) 
        
        # making average
        average= []
        for i in range(6):
            sum = 0 
            for j in range(3):
                sum = sum + marks[j][i]

            sum = round(sum/3,2)
            average.append(sum)
        # print(average)
        print("\nsemester : ",semester,"\n")

        if semester<7:

            listt={
            "Subjects":subjects[0],
            "Midterm 1":marks[0],
            "Midterm 2":marks[1],
            "End semester examination":marks[2],
            "Average":average
            }

        elif semester >= 7:
            listt = {
                "Subjects":[subjects[0][0],subjects[0][1]],
                "Midterm 1":[marks[0][0],marks[0][1]],
                "Midterm 2":[marks[1][0],marks[1][1]],
                "End semester examination":[marks[2][0],marks[2][1]],
                "Average":[average[0],average[1]]
            }

        df = pd.DataFrame(listt)
        print(df)
        semester -= 1
    

    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

def main():
    # sujbects function must run only once 
    # more details on line 30
    while(1):
        system('cls')
        print("PORTAL")
        print("1. Add a student \n2. Enter the marks \n3. Show marksheet \nEnter your choise : ")
        choice = int(input())
        if choice==1:
            add()
        elif choice==2:
            entermarks()
        elif choice==3:
            show()
        elif choice==4 :
            break

main()