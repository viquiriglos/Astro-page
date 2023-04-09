from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine( db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl-ca":"/etc/ssl/cert.pem"
                        }
                      })

def load_courses_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from courses"))
    courses = []
    for row in result.all():
      courses.append(row._asdict())
    return courses

def load_course_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from courses where id = :val"),  {"val" : id})
    rows = result.all()
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()

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
