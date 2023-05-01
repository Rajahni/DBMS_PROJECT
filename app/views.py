from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/register", methods=["POST"])
def register_user():

    try:
        conn = mysql.connector.connect(user="uwi_user",
                                    password="uwi876",
                                    host="localhost",
                                    database="uwi",
                                    auth_plugin='mysql_native_password'
                                    )
        
        cursor = conn.cursor()
        # content = request.json
        cursor.execute(f"SELECT MAX(LecturerID) from Lecturer")
        row = cursor.fetchone()
        lectid = {}
        if row is not None:
            lecturerID = row
            lectid = {}
            lectid["lecturer_id"] = lecturerID
            cursor.close()
            return make_response(lecturerID)
        return 'no'
        # userId = content[]
        # firstname = content['firstname']
        # lastname = content['lastname']
        
        # email = content['email']
        # cursor.execute(f"SELECT * from Student WHERE Email={email}")
        # row = cursor.fetchone()
        # if row is not None:
        #     role = 'student'
        # elif row is None:
        #     cursor.execute(f"SELECT * from Lecturer WHERE Email={email}")
        #     row = cursor.fetchone()
        #     if row is not None:
        #         role = 'lecturer'
        # else:
        #     return make_response({"error":"User is neither student nor lecturer"}, 400)
        
    except Exception as e:
        return make_response({'error': str(e)}, 400)

if __name__ == '__main__':
    app.run(debug=True)