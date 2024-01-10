import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    
def createTableStudent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating student table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE student (
            s_idnumber decimal(6,2) not null,
            s_firstname char(25) not null,
            s_middlename char(25) not null,
            s_lastname char(25) not null,
            s_gender char(25) not null, 
            s_gradelevel decimal(3,0) not null, 
            s_dateofbirth date not null);"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableStudent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate student table")
    
    try:
        sql = """INSERT INTO student (s_idnumber, s_firstname, s_middlename, s_lastname, s_gender, s_gradelevel, s_dateofbirth)
            VALUES (000001, 'Jesus', 'Gerardo', 'Ruiz', 'Male', 11, '1999-05-18'),
            (000002, 'Armando', 'Hernandez', 'Francisco', 'Male', 12, '1997-10-11'),
            (000003, 'Brenda', 'Hailey', 'Zavala', 'Female', 9, '2004-05-11'),
            (000004, 'Annisette', 'Jenna', 'Madsen', 'Female', 10, '2002-01-13'),
            (000005, 'Mia', 'Thermopolis', 'Madsen', 'Female', 10, '2002-01-13'),
            (000006, 'Frendz', 'Megz', 'Caluma', 'Male', 9, '2004-11-02'),
            (000007, 'Regina', 'Sofia', 'Chavez', 'Female', 11, '2001-02-07'),
            (000008, 'Val', 'Zaira', 'Pulido', 'Female', 11, '2002-07-16'),
            (000009, 'Lauren', 'Emily', 'Vierra', 'Female', 11, '2001-01-25'),
            (000010, 'Alfredo', 'Guillermo', 'Moreno', 'Male', 10, '2002-01-12');"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableStudent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping student table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE student"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableContacts(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating contact table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE contacts (
            e_name char(25) not null,
            e_idnumber decimal(6,2) not null,
            e_phonenumber char(15) not null,
            e_relationship char(25) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableContact(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate contact table")
    
    try:
        sql = """INSERT INTO contacts (e_idnumber, e_name, e_phonenumber, e_relationship)
            VALUES (000001, 'Blanca', '(209)111-1111', 'Mother'),
            (000001, 'Jesus', '(209)222-2222', 'Father'),
            (000002, 'Julie', '(209)333-3333', 'Mother'),
            (000002, 'Armando', '(209)444-4444', 'Father'),
            (000003, 'Maria', '(209)555-5555', 'Mother'),
            (000003, 'Josue', '(209)666-6666', 'Father'),
            (000004, 'Caytlin', '(209)777-7777', 'Mother'),
            (000004, 'James', '(209)888-8888', 'Father'),
            (000005, 'Caytlin', '(209)999-9999', 'Mother'),
            (000005, 'James', '(209)101-0101', 'Father'),
            (000006, 'Plani', '(209)121-2121', 'Mother'),
            (000006, 'Jonah', '(209)131-3131', 'Father'),
            (000007, 'Laura', '(209)141-4141', 'Mother'),
            (000007, 'Luis', '(209)151-5151', 'Father'),
            (000008, 'Jane', '(209)161-6161', 'Mother'),
            (000008, 'John', '(209)171-7171', 'Father'),
            (000009, 'Emily', '(209)181-8181', 'Mother'),
            (000009, 'Emilio', '(209)191-9191', 'Father'),
            (000010, 'Rocio', '(209)202-0202', 'Mother'),
            (000010, 'Rafael', '(209)212-1212', 'Father');"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableContact(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping contact table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE contacts"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableSchedule(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating schedule table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE schedule (
            cs_idnumber decimal(6,2) not null,
            cs_classid1 decimal(6,2) not null,
            cs_classid2 decimal(6,2) not null,
            cs_classid3 decimal(6,2) not null,
            cs_classid4 decimal(6,2) not null,
            cs_classid5 decimal(6,2) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableSchedule(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate schedule table")
    
    try:
        sql = """INSERT INTO schedule(cs_idnumber, cs_classid1, cs_classid2, cs_classid3, cs_classid4, cs_classid5)
            VALUES (000001, 111111, 222222, 333333, 888888, 999999),
            (000002, 111111, 222222, 333333, 888888, 666666),
            (000003, 111111, 222222, 555555, 101010, 121212),
            (000004, 111111, 222222, 444444, 777777, 666666),
            (000005, 111111, 222222, 333333, 777777, 999999),
            (000006, 111111, 222222, 555555, 101010, 121212),
            (000007, 111111, 222222, 444444, 888888, 666666),
            (000008, 111111, 222222, 333333, 666666, 999999),
            (000009, 111111, 222222, 444444, 101010, 121212),
            (000010, 111111, 222222, 555555, 666666, 999999);"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableSchedule(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping schedule table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE schedule"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableClasses(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating classes table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE classes (
            c_classid decimal(6,2) not null,
            c_name char(25) not null,
            c_instructor char(25) not null,
            c_units decimal(3,0) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableClasses(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate classes table")
    
    try:
        sql = """INSERT INTO classes(c_classid, c_name, c_instructor, c_units)
            VALUES(111111, 'English', 'Kassidy Sizemore', 4),
            (222222, 'History', 'John Holland', 4),
            (333333, 'Math1', 'James Gonzalez', 4),
            (444444, 'Math2', 'Mike Abejuela', 4),
            (555555, 'Math3', 'Paul Hogan', 4),
            (666666, 'Art', 'Sam Bushman', 4),
            (777777, 'Music', 'Michael Flores', 4),
            (888888, 'Colorguard', 'Shavonn Garcia', 4),
            (999999, 'Cooking', 'Andrew Calzadillas', 4),
            (101010, 'Science', 'Julissa Downey', 4),
            (121212, 'Photography', 'Karla Nuno', 4);"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableClasses(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping classes table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE classes"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableGrades(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating grades table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE grades (
            g_grade decimal(3,0) not null,
            g_idnumber decimal(6,2) not null,
            g_classid decimal(6,2) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableGrades(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate grades table")
    
    try:
        sql = """INSERT INTO grades(g_classid, g_idnumber, g_grade)
            VALUES(111111, 000001, 99),
            (111111, 000002, 90),
            (111111, 000003, 87),
            (111111, 000004, 73),
            (111111, 000005, 58),
            (111111, 000006, 85),
            (111111, 000007, 79),
            (111111, 000008, 82),
            (111111, 000009, 69.9),
            (111111, 000010, 86),
            (222222, 000001, 86),
            (222222, 000002, 69.9),
            (222222, 000003, 82),
            (222222, 000004, 79),
            (222222, 000005, 85),
            (222222, 000006, 58),
            (222222, 000007, 73),
            (222222, 000008, 87),
            (222222, 000009, 90),
            (222222, 000010, 99),
            (333333, 000001, 97),
            (333333, 000002, 94),
            (333333, 000005, 93),
            (333333, 000008, 98),
            (444444, 000004, 75),
            (444444, 000007, 99),
            (444444, 000009, 83),
            (555555, 000003, 87),
            (555555, 000006, 79),
            (555555, 000010, 63),
            (666666, 000002, 99),
            (666666, 000004, 67),
            (666666, 000007, 78),
            (666666, 000008, 84),
            (666666, 000010, 94),
            (777777, 000004, 88),
            (777777, 000005, 71),
            (888888, 000001, 99),
            (888888, 000002, 99),
            (888888, 000007, 99),
            (999999, 000001, 77),
            (999999, 000005, 85),
            (999999, 000008, 65),
            (999999, 000010, 79),
            (101010, 000003, 88),
            (101010, 000006, 78),
            (101010, 000009, 85),
            (121212, 000003, 77),
            (121212, 000006, 80),
            (121212, 000009, 96);"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableGrades(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping grades table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE grades"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableExtracurriculars(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating extracurriculars table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE extracurriculars (
            ex_name char(25) not null,
            ex_idnumber decimal(6,2) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableExtracurriculars(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate extracurriculars table")
    
    try:
        sql = """INSERT INTO extracurriculars(ex_idnumber, ex_name)
            VALUES(000001, 'Soccer'),
            (000001, 'Dance Club'),
            (000002, 'Football'),
            (000002, 'Tennis'),
            (000002, 'Theatre'),
            (000003, 'Golf'),
            (000004, 'Soccer'),
            (000005, 'Football'),
            (000006, 'Tennis'),
            (000007, 'Dance Club'),
            (000007, 'Theatre'),
            (000008, 'Soccer'),
            (000009, 'Football'),
            (000009, 'Tennis'),
            (000010, 'Golf');"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableExtracurriculars(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping extracurriculars table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE extracurriculars"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def createTableSchool(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating school table")
    
    _conn.execute("BEGIN")
    try:
        sql = """CREATE TABLE school (
            sc_name char(25) not null,
            sc_idnumber decimal(6,2) not null,
            sc_address char(25) not null,
            sc_phonenumber char(25) not null
        );"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def populateTableSchool(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate school table")
    
    try:
        sql = """INSERT INTO school(sc_name, sc_idnumber, sc_address, sc_phonenumber)
            VALUES ('Engineering', 000001, '100 University Way', '(209)232-3232'),
            ('Humanities', 000002, '101 University Way', '(209)232-3232'),
            ('Medicine', 000003, '102 University Way', '(209)232-3232'),
            ('Natural Sciences', 000004, '103 University Way', '(209)232-3232'),
            ('Engineering', 000005, '100 University Way', '(209)232-3232'),
            ('Humanities', 000006, '101 University Way', '(209)232-3232'),
            ('Medicine', 000007, '102 University Way', '(209)232-3232'),
            ('Natural Sciences', 000008, '103 University Way', '(209)232-3232'),
            ('Engineering', 000009, '100 University Way', '(209)232-3232'),
            ('Humanities', 000010, '101 University Way', '(209)232-3232');"""
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def dropTableSchool(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping school table")
    
    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE school"
        _conn.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def classSchedules(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students class schedules
    
    try:
        
        header = "{}|{}|{}|{}|{}|{}"
        print((header.format("Student", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5")))
        sql = """SELECT s_firstname as studentName, c1.c_name as class1, c2.c_name as class2, c3.c_name as class3, c4.c_name as class4, c5.c_name as class5
            FROM student, schedule, classes c1, classes c2, classes c3, classes c4, classes c5
            WHERE s_idnumber = cs_idnumber AND 
                cs_classid1 = c1.c_classid AND
                cs_classid2 = c2.c_classid AND
                cs_classid3 = c3.c_classid AND
                cs_classid4 = c4.c_classid AND
                cs_classid5 = c5.c_classid
            GROUP BY studentName;"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}|{}|{}".format(row[0],row[1],row[2],row[3],row[4],row[5])
            print(l)
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def classGrades(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students class schedules with grades
    
    try:
        
        header = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}"
        print((header.format("Student", "Class 1", "Grade", "Class 2", "Grade", "Class 3", "Grade", "Class 4", "Grade", "Class 5", "Grade")))
        sql = """SELECT s_firstname as studentName, 
            c1.c_name as class1, 
            g1.g_grade as grade1, 
            c2.c_name as class2,
            g2.g_grade as grade2, 
            c3.c_name as class3,
            g3.g_grade as grade3, 
            c4.c_name as class4,
            g4.g_grade as grade4, 
            c5.c_name as class5,
            g5.g_grade as grade5
        FROM student, schedule, classes c1, classes c2, classes c3, classes c4, classes c5, grades g1, grades g2, grades g3, grades g4, grades g5
        WHERE s_idnumber = cs_idnumber AND 
            cs_classid1 = g1.g_classid AND
            g1.g_idnumber = s_idnumber AND
            cs_classid1 = c1.c_classid AND
            cs_classid2 = g2.g_classid AND
            g2.g_idnumber = s_idnumber AND
            cs_classid2 = c2.c_classid AND
            cs_classid3 = g3.g_classid AND
            g3.g_idnumber = s_idnumber AND
            cs_classid3 = c3.c_classid AND
            cs_classid4 = g4.g_classid AND
            g4.g_idnumber = s_idnumber AND
            cs_classid4 = c4.c_classid AND
            cs_classid5 = g5.g_classid AND
            g5.g_idnumber = s_idnumber AND
            cs_classid5 = c5.c_classid
        GROUP BY studentName;"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def emergencyContacts(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students with their emergency contacts
    
    try:
        
        header = "{}|{}|{}|{}"
        print((header.format("First Name", "Last Name", "Contact", "Phone Number")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName, e_name as contactName, e_phonenumber as phoneNumber
            FROM student, contacts
            WHERE s_idnumber = e_idnumber
            GROUP BY studentFirstName, contactName;"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}".format(row[0],row[1],row[2],row[3])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def extraCurriculars(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students in an extracurricular
    
    try:
        header = "{}|{}|{}"
        print((header.format("Activity", "First Name", "Last Name")))
        sql = """SELECT ex_name as activity, s_firstname as studentFirstName, s_lastname as studentLastName
            FROM extracurriculars, student
            WHERE ex_idnumber = s_idnumber
            GROUP BY activity, studentFirstName;"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}".format(row[0],row[1],row[2])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def passingGrades(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students' passing grades
    
    try:
        header = "{}|{}|{}|{}"
        print((header.format("First Name", "Last Name", "Grade", "Class")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName, g_grade as studentGrade, c_name as className
            FROM student, grades, classes
            WHERE s_idnumber = g_idnumber AND
                g_classid = c_classid
            GROUP BY className, studentFirstName
            HAVING g_grade >= 70;"""
        cur = _conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}".format(row[0],row[1],row[2],row[3])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def stemStudents(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students in STEM
    
    try:
        header = "{}|{}|{}"
        print((header.format("First Name", "Last Name", "School of")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName, sc_name as schoolOf
            FROM student, school
            WHERE s_idnumber = sc_idnumber AND
                (sc_name = 'Engineering' OR
                sc_name = 'Medicine')
            GROUP BY schoolOf, studentFirstName;"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}".format(row[0],row[1],row[2])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def notStem(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students not in STEM
    
    try:
        header = "{}|{}|{}"
        print((header.format("First Name", "Last Name", "School of")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName, sc_name as schoolOf
            FROM student, school
            WHERE s_idnumber = sc_idnumber AND
                sc_name <> 'Engineering' AND
                sc_name <> 'Medicine'
            GROUP BY schoolOf, studentFirstName;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}".format(row[0],row[1],row[2])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def passingCore(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all students that are passing their core classes
    
    try:
        header = "{}|{}|{}|{}"
        print((header.format("First Name", "Last Name", "English Grade", "History Grade")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName, g1.g_grade as engGrade, g2.g_grade as histGrade
            FROM student, grades g1, grades g2, classes c1, classes c2
            WHERE s_idnumber = g1.g_idnumber AND
                g1.g_classid = c1.c_classid AND
                s_idnumber = g2.g_idnumber AND
                g2.g_classid = c2.c_classid AND
                c1.c_name = 'English' AND
                c2.c_name = 'History'
            GROUP BY studentFirstName, engGrade, histGrade
            HAVING engGrade >= 70 AND
                histGrade >= 70;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}".format(row[0],row[1],row[2],row[3])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def studentInfo(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all basic student info
    
    try:
        
        header = "{}|{}|{}|{}|{}|{}|{}"
        print((header.format("Student ID", "First Name", "Middle Name", "Last Name", "Gender", "Grade", "DOB")))
        sql = """SELECT *
            FROM student;"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}|{}|{}|{}|{}|{}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def maleStudents(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all male students
    
    try:
        header = "{}|{}"
        print((header.format("First Name", "Last Name")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName
            FROM student
            WHERE s_gender = 'Male'
            GROUP BY studentFirstName;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}".format(row[0],row[1])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def femaleStudents(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints all female students
    
    try:
        header = "{}|{}"
        print((header.format("First Name", "Last Name")))
        sql = """SELECT s_firstname as studentFirstName, s_lastname as studentLastName
            FROM student
            WHERE s_gender = 'Female'
            GROUP BY studentFirstName;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}".format(row[0],row[1])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def enrollmentCount(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints number of students enrolled in each class
    
    try:
        header = "{}|{}"
        print((header.format("Class", "Students")))
        sql = """SELECT c_name as className, COUNT(s_firstname) as numStudents
            FROM student, classes, schedule
            WHERE s_idnumber = cs_idnumber AND
                (c_classid = cs_classid1 OR
                c_classid = cs_classid2 OR
                c_classid = cs_classid3 OR
                c_classid = cs_classid4 OR
                c_classid = cs_classid5)
            GROUP BY className;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}".format(row[0],row[1])
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def extraCount(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #prints number of students in each extra curricular
    
    try:
        header = "{}|{}"
        print((header.format("Activity", "Students")))
        sql = """SELECT ex_name as activity, COUNT(s_firstname) as numStudents
            FROM student, extracurriculars
            WHERE s_idnumber = ex_idnumber
            GROUP BY activity;"""
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            l = "{}|{}".format(row[0],row[1])
            print(l)
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def updateGrade(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #updates grade for a class
    
    try:
        firstname = input("What is the first name of the student whose grade you would like to change?  ")
        lastname = input("What is the last name of the student whose grade you would like to change?  ")
        classname = input("What class would you like to change the grade for?  ")
        grade = input("What would you like the new grade to be?  ")
        
        sql = """UPDATE grades
            SET g_grade = ?
            WHERE g_grade = (SELECT g_grade
                FROM grades, classes, student
                WHERE g_classid = c_classid AND
                g_idnumber = s_idnumber AND
                s_firstname = ? AND
                s_lastname = ? AND
                c_name = ?);"""
        cur = _conn.cursor()
        cur.execute(sql, [grade, firstname, lastname, classname])
        
        print("grade has been updated")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def newStudent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    #creates a new student
    
    try:
        idnumber = input("What is the student's id number  ")
        firstname = input("What is the first name of the new student?  ")
        middlename = input("What is the middle name of the new student?  ")
        lastname = input("What is the last name of the new student?  ")
        gender = input("What gender is the new student?  ")
        gradelevel = input("What grade level is the new student? \t")
        dob = input("What is the students date of birth? (Please input in the format yyyy-mm-dd)  ")
        
        sql = """INSERT INTO student (s_idnumber, s_firstname, s_middlename, s_lastname, s_gender, s_gradelevel, s_dateofbirth)
            VALUES (?, ?, ?, ?, ?, ?, ?);"""
        cur = _conn.cursor()
        cur.execute(sql, [idnumber, firstname, middlename, lastname, gender, gradelevel, dob])
        
        print("student has been added")
        
    except Error as e:
        _conn.rollback()
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")
    
def a():
    print("Here is a list of actions you can perform with the app \n")
    print("To see a list of all of the student class schedules, type '1'")
    print("To see a list of all of the student grades, type '2'")
    print("To see a list of all of the emergency contacts, type '3'")
    print("To see a list of all of the students in an extracurricular, type '4'")
    print("To see a list of all of the students with a passing grade in any class, type '5'")
    print("To see a list of all of the students that are a STEM major, type '6'")
    print("To see a list of all of the students that are not a STEM major, type '7'")
    print("To see a list of all of the students who are passing their core classes(English and History), type '8'")
    print("To see a list of basic student information, type '9'")
    print("To see a list of all of the male students, type '10'")
    print("To see a list of all of the female students, type '11'")
    print("To see a list of the enrollment count of each class, type '12'")
    print("To see a list of the enrollment count of each extracurricular, type '13'")
    print("To update a grade, type '14'")
    print("To add a new student, type '15'")
    print("To end the program, type 'q'")
    
def main():
    
    database = r"database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        
        print('Welcome to our Student Roster App \n')
        
        #dropTableStudent(conn)
        #createTableStudent(conn)
        #populateTableStudent(conn)
        
        #dropTableContact(conn)
        #createTableContacts(conn)
        #populateTableContact(conn)
        
        #dropTableSchedule(conn)
        #createTableSchedule(conn)
        #populateTableSchedule(conn)
        
        #dropTableClasses(conn)
        #createTableClasses(conn)
        #populateTableClasses(conn)
        
        #dropTableGrades(conn)
        #createTableGrades(conn)
        #populateTableGrades(conn)
        
        #dropTableExtracurriculars(conn)
        #createTableExtracurriculars(conn)
        #populateTableExtracurriculars(conn)
        
        #dropTableSchool(conn)
        #createTableSchool(conn)
        #populateTableSchool(conn)
        
        print("Here is a list of actions you can perform with the app \n")
        print("To see a list of all of the student class schedules, type '1'")
        print("To see a list of all of the student grades, type '2'")
        print("To see a list of all of the emergency contacts, type '3'")
        print("To see a list of all of the students in an extracurricular, type '4'")
        print("To see a list of all of the students with a passing grade in any class, type '5'")
        print("To see a list of all of the students that are a STEM major, type '6'")
        print("To see a list of all of the students that are not a STEM major, type '7'")
        print("To see a list of all of the students who are passing their core classes(English and History), type '8'")
        print("To see a list of basic student information, type '9'")
        print("To see a list of all of the male students, type '10'")
        print("To see a list of all of the female students, type '11'")
        print("To see a list of the enrollment count of each class, type '12'")
        print("To see a list of the enrollment count of each extracurricular, type '13'")
        print("To update a grade, type '14'")
        print("To add a new student, type '15'")
        print("To end the program, type 'q'")
        
        action = input("Which action would you like to perform?  ")
        
        while action != '':
            if action == '1':
                classSchedules(conn)
            elif action == '2':
                classGrades(conn)
            elif action == '3':
                emergencyContacts(conn)
            elif action == '4':
                extraCurriculars(conn)
            elif action == '5':
                passingGrades(conn)
            elif action == '6':
                stemStudents(conn)
            elif action == '7':
                notStem(conn)
            elif action == '8':
                passingCore(conn)
            elif action == '9':
                studentInfo(conn)
            elif action == '10':
                maleStudents(conn)
            elif action == '11':
                femaleStudents(conn)
            elif action == '12':
                enrollmentCount(conn)
            elif action == '13':
                extraCount(conn)
            elif action == '14':
                updateGrade(conn)
            elif action == '15':
                newStudent(conn)
            elif action == 'a':
                a()
            elif action == 'q':
                break
            else:
                print("Your action was not recognized, please try again")
            
            print("To see the list of commands again, type 'a'")
            action = input("Which action would you like to perform?  ")
        
        #classSchedules(conn)
        #classGrades(conn)
        #emergencyContacts(conn)
        #extraCurriculars(conn)
        #passingGrades(conn)
        #stemStudents(conn)
        #notStem(conn)
        #passingCore(conn)
        #studentInfo(conn)
        #maleStudents(conn)
        #femaleStudents(conn)
        #enrollmentCount(conn)
        #extraCount(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()