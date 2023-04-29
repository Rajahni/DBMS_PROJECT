-- Create the 'project' database if it doesn't exist and use it
CREATE DATABASE IF NOT EXISTS uwi;
USE uwi;

-- Create the 'User' table
CREATE TABLE IF NOT EXISTS User (
	userid INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role ENUM ('admin', 'lecturer', 'student'),
    PRIMARY KEY (userid)
);

-- Create the 'Admin' table
CREATE TABLE IF NOT EXISTS Admin (
	adminid INT NOT NULL AUTO_INCREMENT,
    userid INT,
    PRIMARY KEY (adminid),
    FOREIGN KEY (userid) REFERENCES User(userid)
);

-- Create the 'Lecturer' table
CREATE TABLE IF NOT EXISTS Lecturer (
	lecturerid INT NOT NULL AUTO_INCREMENT,
    userid INT,
    PRIMARY KEY (lecturerid),
    FOREIGN KEY (userid) REFERENCES User(userid)
);

-- Create the 'Student' table
CREATE TABLE IF NOT EXISTS Student (
	studentid INT,
    userid INT,
    PRIMARY KEY (studentid),
    FOREIGN KEY (userid) REFERENCES User(userid)
);

-- Create the 'Course' table
CREATE TABLE IF NOT EXISTS Course (
	courseid INT,
    course_name VARCHAR(255),
    date_created Date,
    adminid INT,
    PRIMARY KEY (courseid),
    FOREIGN KEY (adminid) REFERENCES Admin(adminid)
);

-- Create the 'Section' table
CREATE TABLE IF NOT EXISTS Section (
    sectionid INT,
    courseid INT,
    section_title VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (sectionid),
    FOREIGN KEY (courseid) REFERENCES Course(courseid)
);

-- Create the 'Section_Item' table
CREATE TABLE IF NOT EXISTS Section_Item (
	itemid INT,
    item_type ENUM ('link', 'file', 'slides'),
    item_content VARCHAR(255),
    sectionid INT,
    PRIMARY KEY (itemid),
    FOREIGN KEY (sectionid) REFERENCES Section(sectionid)
);

-- Create the 'Calendar_Event' table
CREATE TABLE IF NOT EXISTS Calendar_Event (
	eventid INT,
    event_name VARCHAR(100),
    event_content VARCHAR(500),
    courseid INT,
    PRIMARY KEY (eventid),
    FOREIGN KEY (courseid) REFERENCES Course(courseid)
);

-- Create the 'Forum' table
CREATE TABLE IF NOT EXISTS Forum (
	forumid INT,
    forum_name VARCHAR(100),
    date_created Date,
    courseid INT,
    PRIMARY KEY (forumid),
    FOREIGN KEY (courseid) REFERENCES Course(courseid)
);

-- Create the 'Discussion' table
CREATE TABLE IF NOT EXISTS Discussion (
	thread_id INT,
    thread_title VARCHAR(100),
    thread_content VARCHAR(500),
    date_created Date,
    forumid INT,
    userid INT,
    PRIMARY KEY (thread_id),
    FOREIGN KEY (forumid) REFERENCES Forum(forumid),
    FOREIGN KEY (userid) REFERENCES User(userid)
);

-- Create the 'Reply' table
CREATE TABLE IF NOT EXISTS Reply (
	reply_id INT,
    reply_title VARCHAR(100),
    reply_content VARCHAR(500),
    date_created Date,
    thread_id INT,
    PRIMARY KEY (reply_id),
    FOREIGN KEY (thread_id) REFERENCES Discussion(thread_id)
);

-- Create the 'Assignment' table
CREATE TABLE IF NOT EXISTS Assignment (
	assignment_id INT,
    assignment_content VARCHAR(255),
    date_created Date,
    due_date Date,
    courseid INT,
    studentid INT,
    lecturerid INT,
    PRIMARY KEY (assignment_id),
    FOREIGN KEY (courseid) REFERENCES Course(courseid),
    FOREIGN KEY (studentid) REFERENCES Student(studentid),
    FOREIGN KEY (lecturerid) REFERENCES Lecturer(lecturerid)
);

-- Create the 'Enrol_Student' table
CREATE TABLE IF NOT EXISTS Enrol_Student (
	enrol_id INT,
    student_id INT,
    courseid INT,
    PRIMARY KEY (enrol_id),
    FOREIGN KEY (student_id) REFERENCES Student(studentid),
    FOREIGN KEY (courseid) REFERENCES Course(courseid)
);

CREATE TABLE IF NOT EXISTS Enrol_Lecturer (
	enrol_id INT,
    lecturerid INT,
    course_id INT,
    PRIMARY KEY (enrol_id),
    FOREIGN KEY (lecturerid) REFERENCES Lecturer(lecturerid),
    FOREIGN KEY (course_id) REFERENCES Course(courseid)
);

CREATE TABLE IF NOT EXISTS Grade (
	gradeid INT,
    grade_score INT,
    lecturerid INT,
    course_id INT,
    student_id INT,
    assignment_id INT,
    PRIMARY KEY (gradeid),
    FOREIGN KEY (lecturerid) REFERENCES Lecturer(lecturerid),
    FOREIGN KEY (course_id) REFERENCES Course(courseid),
    FOREIGN KEY (student_id) REFERENCES Student(studentid),
    FOREIGN KEY (assignment_id) REFERENCES Assignment(assignment_id)
);
