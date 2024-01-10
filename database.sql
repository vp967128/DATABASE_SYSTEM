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
    e_idnumber decimal(6,2) not null,
    e_name char(25) not null,
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
    g_idnumber decimal(6,2) not null,
    g_classid decimal(6,2) not null,
    g_grade decimal(3,0) not null
);

CREATE TABLE extracurriculars (
    ex_idnumber decimal(6,2) not null,
    ex_name char(25) not null
);

CREATE TABLE school (
    sc_name char(25) not null,
    sc_idnumber decimal(6,2) not null,
    sc_address char(25) not null,
    sc_phonenumber char(25) not null
);