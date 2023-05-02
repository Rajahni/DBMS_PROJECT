from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


# Retrieve Courses
@app.route('/courses', methods=['GET'])
def retrieve_courses():
    # retrieve all courses from database
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    cursor.close()
    
    return jsonify(courses), 200

# Retrieve members of a course
@app.route('/students/<string:course_id>', methods=['GET'])
def retrieve_members_of_course(course_id):
    # retrieve all members of specified course from database
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM EnrolStudents WHERE CourseID=%s", (course_id,))
    members = cursor.fetchall()
    cursor.close()
    
    return jsonify(members), 200

# Retrieve calendar events for a course
@app.route('/courses/<course_id>/calendar', methods=['GET'])
def get_calendar_events(course_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Calendar WHERE CourseID=%s", [course_id])
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
        cursor = mysql.connection.cursor()
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
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Discussion WHERE CourseID=%s", [forum_id])
        discussions = cursor.fetchall()
        cursor.close()
        if len(discussions) == 0:
            return jsonify({'message': 'No discussions found for the forum.'}), 404
        return jsonify({'discussions': discussions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)