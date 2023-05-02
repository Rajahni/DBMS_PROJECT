from flask import Flask, request, jsonify
# from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

cursor = cnx.cursor()

# Retrieve All Courses
@app.route('/courses', methods=['GET'])
def retrieve_courses():

    cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

    cursor = cnx.cursor()
    # retrieve all courses from database
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()

    # course_list = {}
    # for course in courses:
    #     course['']
    cursor.close()
    
    return jsonify(courses), 200

# Retrieve courses for a particular student
@app.route('/courses/student/<studentid>', methods=['GET'])
def student_courses(studentid):

    cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

    cursor = cnx.cursor()
    
    cursor.execute(f"SELECT Course.course_name\
                    FROM Course\
                    JOIN Enrol_Student ON Course.courseid = Enrol_Student.courseid\
                    WHERE Enrol_Student.student_id = {studentid}")
    courses = cursor.fetchall()
    cursor.close()
    
    return jsonify(courses), 200

# Retrieve courses taught by a lecturer
@app.route('/courses/lecturer/<lecturerid>', methods=['GET'])
def lecturer_courses(lecturerid):

    cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

    cursor = cnx.cursor()
    
    cursor.execute(f"SELECT Course.course_name\
                    FROM Course\
                    JOIN Enrol_Lecturer ON Course.courseid = Enrol_Lecturer.course_id\
                    WHERE Enrol_Lecturer.lecturerid = {lecturerid}")
    courses = cursor.fetchall()
    cursor.close()
    
    return jsonify(courses), 200

# Retrieve members of a course
@app.route('/students/<course_id>', methods=['GET'])
def retrieve_members_of_course(course_id):
    cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

    cursor = cnx.cursor()
    # retrieve all members of specified course from database
    cursor.execute("SELECT * FROM Enrol_Student WHERE CourseID=%s", (course_id,))
    members = cursor.fetchall()
    cursor.close()
    
    return jsonify(members), 200

# Retrieve calendar events for a course
@app.route('/courses/<course_id>/calendar', methods=['GET'])
def get_calendar_events(course_id):
    try:
        cnx = mysql.connector.connect(
        host="localhost",
        user="uwi_user",
        password="uwi876",
        database="uwi"
        )

        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Calendar_Event WHERE CourseID=%s", [course_id])
        calendar_events = cursor.fetchall()
        cursor.close()
        if len(calendar_events) == 0:
            return jsonify({'message': 'No calendar events found for the course.'}), 404
        return jsonify({'calendar_events': calendar_events}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Retrieve forums for a course
@app.route('/courses/<course_id>/forums', methods=['GET'])
def get_forums(course_id):
    try:
        cursor.execute("SELECT * FROM Forum WHERE CourseID=%s", [course_id])
        forums = cursor.fetchall()
        cursor.close()
        if len(forums) == 0:
            return jsonify({'message': 'No forums found for the course.'}), 404
        return jsonify({'forums': forums}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Retrieve discussion threads for a forum
@app.route('/courses/forum/<forum_id>/discussions', methods=['GET'])
def get_discussions(forum_id):
    try:
        cursor.execute("SELECT * FROM Discussion WHERE CourseID=%s", [forum_id])
        discussions = cursor.fetchall()
        cursor.close()
        if len(discussions) == 0:
            return jsonify({'message': 'No discussions found for the forum.'}), 404
        return jsonify({'discussions': discussions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# All courses that have 50 or more students
@app.route('/courses/fifty_or_more_students', methods=['GET'])
def courses_fifty_or_more_students():
    # retrieve all courses from database that have 50 or more students
    cursor.execute("SELECT Course.courseid, Course.coursename, COUNT(StudentCourse.StudentID) AS EnrolledStudents FROM Course JOIN StudentCourse ON Course.CourseID=StudentCourse.CourseID GROUP BY Course.CourseID HAVING COUNT(StudentCourse.StudentID) >= 50")
    courses = cursor.fetchall()
    
    return jsonify(courses), 200


# All students that do 5 or more courses
@app.route('/students/five_or_more_courses', methods=['GET'])
def students_five_or_more_courses():
    # retrieve all students from database that do 5 or more courses
    cursor.execute("SELECT Student.StudentID, Student.FirstName, Student.LastName, COUNT(StudentCourse.CourseID) AS EnrolledCourses FROM Student JOIN StudentCourse ON Student.StudentID=StudentCourse.StudentID GROUP BY Student.StudentID HAVING COUNT(StudentCourse.CourseID) >= 5")
    students = cursor.fetchall()
    
    return jsonify(students), 200


# All lecturers that teach 3 or more courses
@app.route('/lecturers/three_or_more_courses', methods=['GET'])
def lecturers_three_or_more_courses():
    # retrieve all lecturers from database that teach 3 or more courses
    cursor.execute("SELECT Lecturer.LecturerID, Lecturer.FirstName, Lecturer.LastName, COUNT(Course.LecturerID) AS TeachingCourses FROM Lecturer JOIN Course ON Lecturer.LecturerID=Course.LecturerID GROUP BY Lecturer.LecturerID HAVING COUNT(Course.LecturerID) >= 3")
    lecturers = cursor.fetchall()
    
    return jsonify(lecturers), 200

# The 10 most enrolled courses
@app.route('/courses/most_enrolled', methods=['GET'])
def courses_most_enrolled():
    # retrieve the 10 most enrolled courses from database
    cursor.execute("SELECT Course.CourseID, Course.CourseName, COUNT(StudentCourse.StudentID) AS EnrolledStudents FROM Course JOIN StudentCourse ON Course.CourseID=StudentCourse.CourseID GROUP BY Course.CourseID ORDER BY COUNT(StudentCourse.StudentID) DESC LIMIT 10")
    courses = cursor.fetchall()
    
    return jsonify(courses), 200

# The top 10 students with the highest overall averages
@app.route('/students/highest_averages', methods=['GET'])
def students_highest_averages():
    # retrieve the top 10 students with the highest overall averages from database
    cursor.execute("SELECT Student.StudentID, Student.FirstName, Student.LastName, AVG(Grade) AS AverageGrade FROM Student JOIN StudentCourse ON Student.StudentID=StudentCourse.StudentID JOIN CourseWork ON StudentCourse.StudentCourseID=CourseWork.StudentCourseID GROUP BY Student.StudentID ORDER BY AVG(Grade) DESC LIMIT 10")
    students = cursor.fetchall()
    
    return jsonify(students), 200


@app.route('/courses', methods=['POST'])
def create_course():
    cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
    )

    cursor = cnx.cursor()
    course_name = request.json['course_name']
    
    cursor.execute("INSERT INTO Course (course_name) VALUES (%s)", (course_name,))
    cursor.close()
    
    # return success response
    return jsonify({'message': 'Course created successfully'}), 201

@app.route('/calendar_events', methods=['POST'])
def create_calendar_event():
    cnx = mysql.connector.connect(
        host="localhost",
        user="uwi_user",
        password="uwi876",
        database="uwi"
    )
    cursor = cnx.cursor()

    event_name = request.json['event_name']
    event_content = request.json['event_content']
    courseid = request.json['courseid']
    event_date = request.json['event_date']

    cursor.execute(
        "INSERT INTO Calendar_Event (event_name, event_content, courseid, event_date) VALUES (%s, %s, %s, %s)",
        (event_name, event_content, courseid, event_date)
    )
    cnx.commit()
    cursor.close()
    cnx.close()

    # return success response
    return jsonify({'message': 'Calendar event created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)