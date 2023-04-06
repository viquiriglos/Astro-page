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
