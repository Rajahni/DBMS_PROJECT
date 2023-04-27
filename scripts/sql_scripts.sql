CREATE DATABASE IF NOT EXISTS project;

USE project;

CREATE TABLE IF NOT EXISTS Student (
	StudentID INT,
	Name VARCHAR(500),
	Address VARCHAR(500),
	Email VARCHAR(500),
	PRIMARY KEY (StudentID)
);

CREATE TABLE IF NOT EXISTS Course (
	CourseID VARCHAR(500),
	CourseName VARCHAR(500),
	DateCreated DATE,
	PRIMARY KEY (CourseID)
);

CREATE TABLE IF NOT EXISTS EnrolStudents (
	StudentID INT,
	CourseID VARCHAR(500),
	FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE IF NOT EXISTS EnrolLecturer (
	LecturerID INT,
	CourseID VARCHAR(500),
	FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID)
);

CREATE TABLE IF NOT EXISTS Calendar (
	CalendarID INT,
	CourseID INT,
    Cal_Event VARCHAR(255),
    Cal_Date Date,
	PRIMARY KEY (CalendarID)
);

CREATE TABLE IF NOT EXISTS Forum (
	ForumID INT,
    CourseID INT,
	Forum_Name VARCHAR(100),
    Date_Created Date,
	PRIMARY KEY (ForumID)
);

CREATE TABLE IF NOT EXISTS Discussion (
	DiscussionID INT,
	CourseID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Post Date,
	PRIMARY KEY (DiscussionID)
);

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

CREATE TABLE IF NOT EXISTS Assignments (
	AssignmentID INT,
	CourseID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Post Date,
	PRIMARY KEY (AssignmentID)
);

CREATE TABLE IF NOT EXISTS Grades (
	GradesID INT,
	CourseID INT,
    StudentID INT,
    Grade FLOAT,
	PRIMARY KEY (GradesID)
);

CREATE TABLE IF NOT EXISTS Logins (
	UserID INT,
	Name VARCHAR(100) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Joined_Date Date,
	PRIMARY KEY (UserID)
);




LOAD DATA INFILE '/var/lib/mysql-files/students_full.csv' 
INTO TABLE Student 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/courses.csv' 
INTO TABLE Course
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/Lecturer.csv' 
INTO TABLE Lecturer
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/Lecturer.csv' 
INTO TABLE Lecturer
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/enrol_lecturer.csv' 
INTO TABLE Lecturer
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/enrol_students.csv' 
INTO TABLE Lecturer
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;