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
        cnx = mysql.connector.connect(
        host="localhost",
        user="uwi_user",
        password="uwi876",
        database="uwi"
        )

        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Forum WHERE CourseID=%s", [course_id])
        forums = cursor.fetchall()
        cursor.close()
        if len(forums) == 0:
            return jsonify({'message': 'No forums found for the course.'}), 404
        return jsonify({'forums': forums}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Retrieve discussion threads for a forum


# All courses that have 50 or more students
@app.route('/courses/fifty_or_more_students', methods=['GET'])
def courses_fifty_or_more_students():
    # retrieve all courses from database that have 50 or more students
    cursor.execute("SELECT Course.courseid, Course.course_name, COUNT(Enrol_Student.student_id) AS num_students FROM Course INNER JOIN Enrol_Student ON Course.courseid = Enrol_Student.courseid GROUP BY Course.courseid HAVING COUNT(Enrol_Student.student_id) >= 50;")
    courses = cursor.fetchall()
    
    return jsonify(courses), 200


# All students that do 5 or more courses
@app.route('/students/five_or_more_courses', methods=['GET'])
def students_five_or_more_courses():
    # retrieve all students from database that do 5 or more courses
    cursor.execute("SELECT Student.studentid, COUNT(Enrol_Student.courseid) AS num_courses FROM Student INNER JOIN Enrol_Student ON Student.studentid = Enrol_Student.student_id GROUP BY Student.studentid HAVING COUNT(Enrol_Student.courseid) >= 5;")
    students = cursor.fetchall()
    
    return jsonify(students), 200


# All lecturers that teach 3 or more courses
@app.route('/lecturers/three_or_more_courses', methods=['GET'])
def lecturers_three_or_more_courses():
    # retrieve all lecturers from database that teach 3 or more courses
    cursor.execute("SELECT Lecturer.lecturerid, COUNT(Enrol_Lecturer.course_id) AS num_courses FROM Lecturer INNER JOIN Enrol_Lecturer ON Lecturer.lecturerid = Enrol_Lecturer.lecturerid GROUP BY Lecturer.lecturerid HAVING COUNT(Enrol_Lecturer.course_id) >= 3;")
    lecturers = cursor.fetchall()
    
    return jsonify(lecturers), 200

# The 10 most enrolled courses
@app.route('/courses/most_enrolled', methods=['GET'])
def courses_most_enrolled():
    # retrieve the 10 most enrolled courses from database
    cursor.execute("SELECT c.course_name, COUNT(*) AS enrolment_count\
                    FROM Enrol_Student e\
                    INNER JOIN Course c ON e.courseid = c.courseid\
                    GROUP BY c.courseid\
                    ORDER BY enrolment_count DESC\
                    LIMIT 10;")
    courses = cursor.fetchall()
    
    return jsonify(courses), 200

# The top 10 students with the highest overall averages
@app.route('/students/highest_averages', methods=['GET'])
def students_highest_averages():
    # retrieve the top 10 students with the highest overall averages from database
    cursor.execute("SELECT Enrol_Student.courseid, COUNT(*) as num_students FROM Enrol_Student JOIN Course ON Enrol_Student.courseid = Course.courseid GROUP BY Enrol_Student.courseid ORDER BY num_students DESC LIMIT 10;")
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
    
    cursor.execute(f"INSERT INTO Course (course_name) VALUES ('{course_name}')")
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
        "INSERT INTO Calendar_Event (event_name, event_content, courseid, event_date) VALUES\
        ('{event_name}', '{event_content}', '{courseid}', '{event_date}')"
    )
    cnx.commit()
    cursor.close()
    cnx.close()

    # return success response
    return jsonify({'message': 'Calendar event created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)