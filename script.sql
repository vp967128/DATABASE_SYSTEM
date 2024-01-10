CREATE TABLE student (
    s_idnumber decimal(6,2) not null,
    s_firstname char(25) not null,
    s_middlename char(25) not null,
    s_lastname char(25) not null,
    s_gender char(25) not null, 
    s_gradelevel decimal(3,0) not null, 
    s_dateofbirth date not null
);

CREATE TABLE contacts (
    e_name char(25) not null,
    e_idnumber decimal(6,2) not null,
    e_phonenumber char(15) not null,
    e_relationship char(25) not null
);

CREATE TABLE schedule (
    cs_idnumber decimal(6,2) not null,
    cs_classid1 decimal(6,2) not null,
    cs_classid2 decimal(6,2) not null,
    cs_classid3 decimal(6,2) not null,
    cs_classid4 decimal(6,2) not null,
    cs_classid5 decimal(6,2) not null
);

CREATE TABLE classes (
    c_classid decimal(6,2) not null,
    c_name char(25) not null,
    c_instructor char(25) not null,
    c_units decimal(3,0) not null
);

CREATE TABLE grades (
    g_grade decimal(3,0) not null,
    g_idnumber decimal(6,2) not null,
    g_classid decimal(6,2) not null
);

CREATE TABLE extracurriculars (
    ex_name char(25) not null,
    ex_idnumber decimal(6,2) not null
);

CREATE TABLE school (
    sc_name char(25) not null,
    sc_idnumber decimal(6,2) not null,
    sc_address char(25) not null,
    sc_phonenumber char(25) not null
);

INSERT INTO student (s_idnumber, s_firstname, s_middlename, s_lastname, s_gender, s_gradelevel, s_dateofbirth)
VALUES (000001, 'Jesus', 'Gerardo', 'Ruiz', 'Male', 11, '1999-05-18'),
(000002, 'Armando', 'Hernandez', 'Francisco', 'Male', 12, '1997-10-11'),
(000003, 'Brenda', 'Hailey', 'Zavala', 'Female', 9, '2004-05-11'),
(000004, 'Annisette', 'Jenna', 'Madsen', 'Female', 10, '2002-01-13'),
(000005, 'Mia', 'Thermopolis', 'Madsen', 'Female', 10, '2002-01-13'),
(000006, 'Frendz', 'Megz', 'Caluma', 'Male', 9, '2004-11-02'),
(000007, 'Regina', 'Sofia', 'Chavez', 'Female', 11, '2001-02-07'),
(000008, 'Val', 'Zaira', 'Pulido', 'Female', 11, '2002-07-16'),
(000009, 'Lauren', 'Emily', 'Vierra', 'Female', 11, '2001-01-25'),
(000010, 'Alfredo', 'Guillermo', 'Moreno', 'Male', 10, '2002-01-12');

INSERT INTO contacts (e_idnumber, e_name, e_phonenumber, e_relationship)
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
(000010, 'Rafael', '(209)212-1212', 'Father');

INSERT INTO schedule(cs_idnumber, cs_classid1, cs_classid2, cs_classid3, cs_classid4, cs_classid5)
VALUES (000001, 111111, 222222, 333333, 888888, 999999),
(000002, 111111, 222222, 333333, 888888, 666666),
(000003, 111111, 222222, 555555, 101010, 121212),
(000004, 111111, 222222, 444444, 777777, 666666),
(000005, 111111, 222222, 333333, 777777, 999999),
(000006, 111111, 222222, 555555, 101010, 121212),
(000007, 111111, 222222, 444444, 888888, 666666),
(000008, 111111, 222222, 333333, 666666, 999999),
(000009, 111111, 222222, 444444, 101010, 121212),
(000010, 111111, 222222, 555555, 666666, 999999);

INSERT INTO classes(c_classid, c_name, c_instructor, c_units)
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
(121212, 'Photography', 'Karla Nuno', 4);

INSERT INTO grades(g_classid, g_idnumber, g_grade)
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
(121212, 000009, 96);

INSERT INTO extracurriculars(ex_idnumber, ex_name)
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
(000010, 'Golf');

INSERT INTO school(sc_name, sc_idnumber, sc_address, sc_phonenumber)
VALUES ('Engineering', 000001, '100 University Way', '(209)232-3232'),
('Humanities', 000002, '101 University Way', '(209)232-3232'),
('Medicine', 000003, '102 University Way', '(209)232-3232'),
('Natural Sciences', 000004, '103 University Way', '(209)232-3232'),
('Engineering', 000005, '100 University Way', '(209)232-3232'),
('Humanities', 000006, '101 University Way', '(209)232-3232'),
('Medicine', 000007, '102 University Way', '(209)232-3232'),
('Natural Sciences', 000008, '103 University Way', '(209)232-3232'),
('Engineering', 000009, '100 University Way', '(209)232-3232'),
('Humanities', 000010, '101 University Way', '(209)232-3232');

--prints class schedule
SELECT s_firstname as studentName, c1.c_name as class1, c2.c_name as class2, c3.c_name as class3, c4.c_name as class4, c5.c_name as class5
FROM student, schedule, classes c1, classes c2, classes c3, classes c4, classes c5
WHERE s_idnumber = cs_idnumber AND 
    cs_classid1 = c1.c_classid AND
    cs_classid2 = c2.c_classid AND
    cs_classid3 = c3.c_classid AND
    cs_classid4 = c4.c_classid AND
    cs_classid5 = c5.c_classid
GROUP BY studentName

--prints grades for each class
SELECT s_firstname as studentName, 
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
GROUP BY studentName

--prints student name and emergency contacts
SELECT s_firstname as studentFirstName, s_lastname as studentLastName, e_name as contactName, e_phonenumber as phoneNumber
FROM student, contacts
WHERE s_idnumber = e_idnumber
GROUP BY studentFirstName, contactName

--prints everyone in an extracurricular
SELECT ex_name as activity, s_firstname as studentFirstName, s_lastname as studentLastName
FROM extracurriculars, student
WHERE ex_idnumber = s_idnumber
GROUP BY activity, studentFirstName

--prints everyone with a passing grade in a class
SELECT s_firstname as studentFirstName, s_lastname as studentLastName, g_grade as studentGrade, c_name as className
FROM student, grades, classes
WHERE s_idnumber = g_idnumber AND
    g_classid = c_classid
GROUP BY className, studentFirstName
HAVING g_grade >= 70

--prints all of the students in STEM
SELECT s_firstname as studentFirstName, s_lastname as studentLastName, sc_name as schoolOf
FROM student, school
WHERE s_idnumber = sc_idnumber AND
    (sc_name = 'Engineering' OR
    sc_name = 'Medicine')
GROUP BY schoolOf, studentFirstName

--prints all students not in STEM
SELECT s_firstname as studentFirstName, s_lastname as studentLastName, sc_name as schoolOf
FROM student, school
WHERE s_idnumber = sc_idnumber AND
    sc_name <> 'Engineering' AND
    sc_name <> 'Medicine'
GROUP BY schoolOf, studentFirstName

--prints students that are passing core classes (english and history)
SELECT s_firstname as studentFirstName, s_lastname as studentLastName, g1.g_grade as engGrade, g2.g_grade as histGrade
FROM student, grades g1, grades g2, classes c1, classes c2
WHERE s_idnumber = g1.g_idnumber AND
    g1.g_classid = c1.c_classid AND
    s_idnumber = g2.g_idnumber AND
    g2.g_classid = c2.c_classid AND
    c1.c_name = 'English' AND
    c2.c_name = 'History'
GROUP BY studentFirstName, engGrade, histGrade
HAVING engGrade >= 70 AND
    histGrade >= 70

--prints basic student information for each student
SELECT *
FROM student

--prints all of the male students
SELECT s_firstname as studentFirstName, s_lastname as studentLastName
FROM student
WHERE s_gender = 'Male'
GROUP BY studentFirstName

--prints all of the female students
SELECT s_firstname as studentFirstName, s_lastname as studentLastName
FROM student
WHERE s_gender = 'Female'
GROUP BY studentFirstName

--counts the number of students enrolled in each class
SELECT c_name as className, COUNT(s_firstname) as numStudents
FROM student, classes, schedule
WHERE s_idnumber = cs_idnumber AND
    (c_classid = cs_classid1 OR
    c_classid = cs_classid2 OR
    c_classid = cs_classid3 OR
    c_classid = cs_classid4 OR
    c_classid = cs_classid5)
GROUP BY className

--counts the number of students in each extracurricular
SELECT ex_name as activity, COUNT(s_firstname) as numStudents
FROM student, extracurriculars
WHERE s_idnumber = ex_idnumber
GROUP BY activity

--update a student grade
UPDATE grades
SET g_grade = 87
WHERE g_grade = (SELECT g_grade
    FROM grades, classes, student
    WHERE g_classid = c_classid AND
    g_idnumber = s_idnumber AND
    s_firstname = "Alfredo" AND
    s_lastname = "Moreno" AND
    c_name = "English")