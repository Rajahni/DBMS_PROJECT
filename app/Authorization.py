from flask import Blueprint, jsonify, make_response, request, g 
import mysql.connector 
from middleware import is_role, requires_auth 

from utils import create_access_token, get_password_hash, verify_password 

auth = Blueprint("auth", __name__, url_prefix="/auth") 


@auth.route("/register", methods=["POST"]) 
@requires_auth 
@is_role(["admin"]) 
def register(): 
    try: 
        cnx = mysql.connector.connect( 
            user="uwi_user", password="uwi876", host="127.0.0.1", database="uwi" 
        ) 

        cursor = cnx.cursor() 
        content = request.json
        
        id = content["userId"]
        first_name = content["first_name"] 
        last_name = content["last_name"] 
        email = content["email"] 
        role = content["role"] 
        password = get_password_hash(content["password"]) 

        cursor.execute( 
            f"INSERT INTO User VALUES('{id}','{first_name}','{last_name}','{email}','{password}','{role}')" 
        ) 
        cnx.commit() 

        cursor.execute( 
            f"INSERT INTO {role}({role}Id) VALUES('{id}')" 
        ) 
        cnx.commit() 
        cursor.close() 
        cnx.close() 
        return make_response({"success": "Account created"}, 201) 
    except Exception as e: 
        return make_response({"error": str(e)}, 400) 


@auth.route("/login", methods=["POST"]) 
def login(): 
    try: 
        cnx = mysql.connector.connect( 
            user="uwi_user", password="uwi876", host="127.0.0.1", database="uwi" 
        ) 
        cursor = cnx.cursor() 
        content = request.json 
        id = content["userId"] 
        password = content["password"] 

        cursor.execute(f"SELECT * FROM Account WHERE accountID={id}") 

        row = cursor.fetchone() 
        hashed_password = row[-2] 

        is_password_correct = verify_password(password, hashed_password) 

        if not is_password_correct: 
            return make_response({"error": "Incorrect credentials"}, 400) 
        token = create_access_token({"id": row[0]}) 

        cursor.close() 
        cnx.close() 

        return make_response({"success": "Logged in successfully", "token": token}, 201) 
    except Exception as e: 
        return make_response({"error": str(e)}, 400)
    


if __name__ == '__main__':
    auth.run(debug=True)