from sqlalchemy import create_engine, text
import os

# setting up the secret key and connection to DB
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine( db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl-ca":"/etc/ssl/cert.pem"
                        }
                      })

# function for loading the courses from the DB
def load_courses_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from courses"))
    courses = []
    for row in result.all():
      courses.append(row._asdict())
    return courses

# function for loading the information of a specific course from the courses Table
def load_course_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from courses where id = :val"),  {"val" : id})
    rows = result.all()
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()

# function for inserting the submitted values into the DB
def add_application_to_db(course_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications(course_id, first_names, last_names, email, birth_date, birth_place, observations) VALUES (:course_id, :first_names, :last_names, :email, :birth_date, :birth_place, :observations)")
    conn.execute(query,
                 {"course_id" : course_id,
                 "first_names" : data['first_names'],
                 "last_names" : data['last_names'],
                 "email" : data['email'],
                 "birth_date" : data['birth_date'],
                 "birth_place" : data['birth_place'],
                 "observations" : data['observations']}
                )

# function for the API to show each registered person by his/her ID in applications Table
def load_registered_person_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from applications where id = :val"),  {"val" : id})
    rows = result.all()
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()
