from flask import Flask, render_template, jsonify, request
from database import load_courses_from_db, load_course_from_db, add_application_to_db, load_registered_person_from_db


app=Flask(__name__)

@app.route("/")
def hello_world():
  courses_db = load_courses_from_db()
  return render_template('home.html',
                          courses=courses_db)
  
# API to show the list of courses or webinars, in json format
@app.route("/api/courses")
def courses_list():
  courses_db = load_courses_from_db()
  return jsonify(courses_db)

# API to show a course or webinar by ID number, in json format
@app.route("/api/courses/<id>")
def show_course_json(id):
  course = load_course_from_db(id)
  return jsonify(course)

# API to show a person that is registered to a course or webinar by ID number, in json format
@app.route("/api/registration/<id>")
def show_registration_json(id):
  person = load_registered_person_from_db(id)
  return jsonify(person)

@app.route("/courses/<id>")
def show_course(id):
  course_db = load_course_from_db(id)
  if not course_db:
    return "Not Found", 404
  return render_template("coursepage.html", course = course_db)

@app.route("/courses/<id>/apply", methods=['post'])
def apply_to_course(id):
  data = request.form
  course_db = load_course_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application = data,
                         course = course_db)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)