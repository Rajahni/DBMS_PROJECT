import mysql.connector
from faker import Faker
import random

# # Connect to the database
# cnx = mysql.connector.connect(
#     host="your_host_name",
#     user="your_username",
#     password="your_password",
#     database="uwi"
# )

# # Generate 100,102 fake users
# fake = Faker()
# users = []
# for i in range(1,100001):
#     userid = i
#     name = fake.name()
#     email = fake.email()
#     password = fake.password()
#     if i < 100000:
#         role = 3
#     elif i < 100101:
#         role = 2
#     role = 1
#     users.append((userid,name, email, password))

# # Insert the users into the database in batches of 1,000
# cursor = cnx.cursor(prepared=True)
# for i in range(0, 100000, 1000):
#     batch = users[i:i+1000]
#     query = "INSERT INTO User (userid, name, email, password) VALUES (%s, %s, %s, %s)"
#     cursor.executemany(query, batch)
#     cnx.commit()

# # Close the cursor and connection
# cursor.close()
# cnx.close()


# cnx = mysql.connector.connect(
#     host="your_host_name",
#     user="your_username",
#     password="your_password",
#     database="uwi"
# )


# fake = Faker()
# users = []
# for i in range(1,201):
#     userid = i
#     name = fake.name()
#     email = fake.email()
#     password = fake.password()
#     if i < 100000:
#         role = 3
#     elif i < 100101:
#         role = 2
#     role = 1
#     users.append((userid,name, email, password))


random_num = random.randint(1000, 3999)

course_codes = ['MATH', 'ENGL', 'PHYS', 'CHEM', 'HIST',
                'PSYC', 'BIOL', 'CS', 'ECON', 'ART', 'PHIL', 'STAT',
                'ANTH', 'SOC', 'MUSC', 'SPAN', 'COMM', 'GEOL', 'ARCH', 'FREN']

courses = []

for i in range(1, 201):

    courses += [item + str(random_num) for item in course_codes]

coursefordb = []
for i in range(1, len(courses)+1):
    coursefordb.append((i,courses[i-1]))

cnx = mysql.connector.connect(
    host="localhost",
    user="uwi_user",
    password="uwi876",
    database="uwi"
)

# Insert the users into the database in batches of 1,000
cursor = cnx.cursor(prepared=True)
for i in range(1, 201):
    batch = coursefordb[i:i+1000]
    query = "INSERT INTO Course (courseid, course_name) VALUES (%s, %s)"
    cursor.executemany(query, batch)
    cnx.commit()


