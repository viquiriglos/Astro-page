from flask import Flask, render_template, jsonify

app=Flask(__name__)

COURSES = [
  {
  'id':1,
  'title':'Module 1',
  'teacher': 'Maria',
  'topics': 'Elements, Modalities, Signs',
  'duration': '3 months',
  'price': '100 (U$S)'
  },
  {
  'id':2,
  'title':'Module 2',
  'teacher': 'Robert',
  'topics': 'Plantets and Aspects',
  'duration': '3 months',
  'price': '100 (U$S)'
  },
  {
  'id':3,
  'title':'Module 3',
  'teacher': 'Pedro',
  'topics': 'Planets in each Sign',
  'duration': '3 months',
  'price': '100 (U$S)'
  },
  {
  'id':4,
  'title':'Module 4',
  'teacher': 'Stephen',
  'topics': 'Integrating the Natal Chart',
  'duration': '3 months',
  'price': '100 (U$S)'
  },
  {
  'id':5,
  'title':'Module 5',
  'teacher': 'Stephen',
  'topics': 'Making Predictions: Progressions and Transits',
  'duration': '3 months',
  'price': '100 (U$S)'
  },
  {
  'id':6,
  'title':'Webinar 1',
  'teacher': 'Robert',
  'topics': 'Astrology for Political Predictions',
  'duration': '3 hours',
  'price': '75 (U$S)'
  },
  {
  'id':7,
  'title':'Webinar 2',
  'teacher': 'Robert',
  'topics': 'How to analyze the Solar Return Chart',
  'duration': '3 hours',
  'price': '75 (U$S)'
  },
  {
  'id':8,
  'title':'Seminar 3',
  'teacher': 'Robert',
  'topics': 'World Astrology',
  'duration': '3 hours',
  'price': '75 (U$S)'
  }
] 

@app.route("/")
def hello_world():
    return render_template('home.html',
                          courses=COURSES)

@app.route("/api/courses")
def courses_list():
    return jsonify(COURSES)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)