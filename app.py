from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'
app.config['SQL_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Student_identity_details(db.Model):
	student_id = db.Column(db.Integer,primary_key = True)
	student_enrollments = db.Column(db.String(40),nullable = False)
	student_name = db.Column(db.String(50),unique = True,nullable = False)
	student_roll_no = db.Column(db.Integer,unique = True,nullable = False)
	student_password = db.Column(db.String(30),nullable=False)

	def __repr__(self):
		return f"Student:'{self.student_id}','{self.student_name}','{self.student_roll_no}'"

class Teacher_identity_details(db.Model):
	teacher_id = db.Column(db.Integer,primary_key = True)
	teacher_name = db.Column(db.String(50),unique = True,nullable = False)
	teacher_password = db.Column(db.String(30),nullable=False)

	def __repr__(self):
		return f"Student:'{self.teacher_id}','{self.teacher_name}'"

class Teacher_role(db.Model):
	content_id = db.Column(db.Integer,primary_key = True)
	subject_contents = db.Column(db.Text)
	subject = db.Column(db.String(20),nullable=False)
	date_posted = db.Column(db.DateTime,nullable=False,default = datetime.utcnow)
 
	def __repr__(self):
		return f"Student:'{self.subject}','{self.date_posted}'"

class Subject_details(db.Model):
	subject_id = db.Column(db.Integer,primary_key = True)
	subject_name = db.Column(db.String(40),nullable=False)
	student_enrolled = db.Column(db.String(40),nullable=False)
	teacher_assigned = db.Column(db.String(40),nullable=False)

	def __repr__(self):
		return f"Student:'{self.subject_name}','{self.teacher_assigned}'"

class Organization_details(db.Model):
	organization_id = db.Column(db.Integer,primary_key = True)
	organization_password = db.Column(db.String(30),nullable=False)

	def __repr__(self):
		return f"Student:'{self.organization_id}'"
@app.route("/")
@app.route("/organization")
def organization():
    return render_template('organization.html')

@app.route("/browse_catalouge")
def browse_catalouge():
	return render_template('browse_catalouge.html')

if __name__ == '__main__':
	app.run(debug = True)