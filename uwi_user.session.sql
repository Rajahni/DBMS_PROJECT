CREATE TRIGGER check_enrolment_limits
BEFORE INSERT ON Enrol_Student
FOR EACH ROW
BEGIN
    DECLARE course_count INT;
    SELECT COUNT(*) INTO course_count
    FROM Enrol_Student
    WHERE student_id = NEW.student_id;
    IF course_count >= 6 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Maximum number of courses per student exceeded.';
    ELSEIF course_count < 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Minimum number of courses per student not reached.';
    END IF;
END;

CREATE TRIGGER check_teaching_limits
BEFORE INSERT ON Enrol_Lecturer
FOR EACH ROW
BEGIN
    DECLARE course_count INT;
    SELECT COUNT(*) INTO course_count
    FROM Enrol_Lecturer
    WHERE lecturerid = NEW.lecturerid;
    IF course_count >= 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Maximum number of courses per lecturer exceeded.';
    ELSEIF course_count < 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Minimum number of courses per lecturer not reached.';
    END IF;
END;

CREATE TRIGGER check_course_members
BEFORE INSERT ON Enrol_Student
FOR EACH ROW
BEGIN
    DECLARE member_count INT;
    SELECT COUNT(*) INTO member_count
    FROM Enrol_Student
    WHERE courseid = NEW.courseid;
    IF member_count < 10 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Course must have at least 10 members.';
    END IF;
END;

insert into Forum values (1, "To Test Data", "2023-05-02", 5);
insert into Discussion values (1, 'This was very hard', 'This stressed me to near death', "2023-05-02", 1, 8);
insert into Calendar_Event values (1, 'I hope we get marked and pass this course', 'By the sweat of our brow, this is tough', 7);


-- Test that a student can not do more than 6 courses
insert into Enrol_Student values (450403,620000004,1);

-- Test that a student can not do more than 6 courses
insert into Enrol_Lecturer values (302,520000003,1);


-- Test that a student can not do less than 6 courses
-- DELETE FROM Enrol_Student
-- WHERE enrol_id = 29;
