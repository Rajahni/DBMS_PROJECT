-- Create the 'project' database if it doesn't exist and use it
CREATE DATABASE IF NOT EXISTS uwi;
USE uwi;

-- Create the 'Student' table
CREATE TABLE IF NOT EXISTS Student (
    StudentID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Address VARCHAR(500),
    Email VARCHAR(500),
    PRIMARY KEY (StudentID)
);

-- Create the 'Lecturer' table
CREATE TABLE IF NOT EXISTS Lecturer (
    LecturerID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Address VARCHAR(500),
    Email VARCHAR(500),
    PRIMARY KEY (LecturerID)
);

-- Create the 'Course' table
CREATE TABLE IF NOT EXISTS Course (
    CourseID VARCHAR(500),
    CourseName VARCHAR(500),
    DateCreated DATE,
    PRIMARY KEY (CourseID)
);

-- Create the 'EnrolStudents' table and set a foreign key to the 'Student' table
CREATE TABLE IF NOT EXISTS EnrolStudents (
    StudentID INT,
    CourseID VARCHAR(500)
    -- FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

-- Create the 'EnrolLecturer' table and set a foreign key to the 'Lecturer' table
CREATE TABLE IF NOT EXISTS EnrolLecturer (
    LecturerID INT,
    CourseID VARCHAR(500)
    -- FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID)
);

-- Create the 'Calendar' table
CREATE TABLE IF NOT EXISTS Calendar (
    CalendarID INT,
    CourseID INT,
    Cal_Event VARCHAR(255),
    Cal_Date Date,
    PRIMARY KEY (CalendarID)
);

-- Create the 'Forum' table
CREATE TABLE IF NOT EXISTS Forum (
    ForumID INT,
    CourseID INT,
    Forum_Name VARCHAR(100),
    Date_Created Date,
    PRIMARY KEY (ForumID)
);

-- Create the 'Discussion' table
CREATE TABLE IF NOT EXISTS Discussion (
    DiscussionID INT,
    CourseID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Post Date,
    PRIMARY KEY (DiscussionID)
);

-- Create the 'CourseContent' table
CREATE TABLE IF NOT EXISTS CourseContent (
    ContentID INT,
    CourseID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Post Date,
    Links VARCHAR(500),
    Files VARCHAR(500),
    Slides VARCHAR(500),
    PRIMARY KEY (ContentID)
);

-- Create the 'Assignments' table
CREATE TABLE IF NOT EXISTS Assignments (
    AssignmentID INT,
    CourseID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Post Date,
    PRIMARY KEY (AssignmentID)
);

-- Create the 'Grades' table
CREATE TABLE IF NOT EXISTS Grades (
    GradesID INT,
    CourseID INT,
    StudentID INT,
    Grade FLOAT,
    PRIMARY KEY (GradesID)
);

-- Create the 'User' table
CREATE TABLE IF NOT EXISTS User (
    userId INT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(200),
    role VARCHAR(10),
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (userId)
);

-- Load data from 'students_full.csv' into the 'Student' table
LOAD DATA INFILE '/var/lib/mysql-files/Students.csv' 
INTO TABLE Student 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Load data from 'students_full.csv' into the 'Student' table
LOAD DATA INFILE '/var/lib/mysql-files/Lecturers.csv' 
INTO TABLE Lecturer 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Load data from 'courses.csv' into the 'Course' table
LOAD DATA INFILE '/var/lib/mysql-files/courses.csv' 
INTO TABLE Course
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load data from the enrol_lecturer.csv file into the EnrolLecturer table
LOAD DATA INFILE '/var/lib/mysql-files/enrol_lecturer.csv' 
INTO TABLE EnrolLecturer
FIELDS TERMINATED BY ',' -- specifies the delimiter for the fields in the CSV file
OPTIONALLY ENCLOSED BY '"' -- specifies the character used to enclose fields that contain the delimiter
LINES TERMINATED BY '\r\n' -- specifies the line separator used in the CSV file
IGNORE 1 ROWS; -- specifies to ignore the first row of the CSV file, which is typically a header row

-- Load data from the enrol_students.csv file into the EnrolStudents table
LOAD DATA INFILE '/var/lib/mysql-files/enrol_students.csv' 
INTO TABLE EnrolStudents
FIELDS TERMINATED BY ',' -- specifies the delimiter for the fields in the CSV file
OPTIONALLY ENCLOSED BY '"' -- specifies the character used to enclose fields that contain the delimiter
LINES TERMINATED BY '\r\n' -- specifies the line separator used in the CSV file
IGNORE 1 ROWS; -- specifies to ignore the first row of the CSV file, which is typically a header row