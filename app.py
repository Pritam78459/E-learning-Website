from flask import Flask, render_template, flash, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import StudentLogin, TeacherLogin, OrganizationLogin, AddStaff, EditStaffDetails, RemoveStaff, AddStudent, RemoveStudent, MakeClasses, EditStudentDetails

app = Flask(__name__)
app.debug = True
app.secret_key = '9a7c444be3c173a8ffd3fe77b52d2ecf'
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
@app.route("/main")
def main():
	return render_template("main.html")

@app.route("/student_login",methods = ["GET","POST"])
def student_login():
	form = StudentLogin()
	if form.validate_on_submit():
		if form.email.data == 'test_student@gmail.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('student_browse_catalouge'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template("Student_login.html",form = form)

@app.route("/teacher_login",methods = ["GET","POST"])
def teacher_login():
	form  = TeacherLogin()
	if form.validate_on_submit():
		if form.email.data == 'test_teacher@gmail.com' and form.password.data == 'password':
		    flash('You have been logged in!', 'success')
		    return redirect(url_for('teacher_browse_catalouge'))
		else:
		    flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template("teacher_login.html",form = form)

@app.route("/organization_login",methods = ["GET","POST"])
def organization_login():
	form  = OrganizationLogin()
	if form.validate_on_submit():
		if form.email.data == 'test_organization@gmail.com' and form.password.data == 'password':
		    flash('You have been logged in!', 'success')
		    return redirect(url_for('organization'))
		else:
		    flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template("organization_login.html",form = form)

@app.route("/organization")
def organization():
	return render_template("organization.html")

@app.route("/add_staff",methods = ["GET","POST"])
def add_staff():
	form = AddStaff()
	if form.validate_on_submit():
		flash('Teacher added successfully', 'success')
	return render_template("add_staff.html",form = form)

@app.route("/edit_staff")
def edit_staff():
	return render_template("edit_staff.html")

@app.route("/edit_staff_details",methods = ["GET","POST"])
def edit_staff_details():
	form = EditStaffDetails()
	if form.validate_on_submit():
		flash('Teacher details changed successfully', 'success')
	return render_template("edit_staff_details.html",form = form)

@app.route("/make_classes",methods = ["GET","POST"])
def make_classes():
	form = MakeClasses()
	if form.validate_on_submit():
		flash('Subject added successfully', 'success')
	return render_template("make_classes.html",form = form)

@app.route("/remove_staff",methods = ["GET","POST"])
def remove_staff():
	form = RemoveStaff()
	if form.validate_on_submit():
		flash('Teacher remove successfully', 'success')
	return render_template("remove_staff.html",form = form)

@app.route("/student_browse_catalouge")
def student_browse_catalouge():
	return render_template("student_browse_catalouge.html")

@app.route("/teacher_browse_catalouge")
def teacher_browse_catalouge():
	return render_template("teacher_browse_catalouge.html")

@app.route("/grade")
def grade():
	return render_template("grade.html")

@app.route("/course_details")
def course_details():
	return render_template("course_details.html")

@app.route("/student_details")
def student_details():
	return render_template("index.html")

@app.route("/teacher_details")
def teacher_details():
	return render_template("teacher_details.html")

@app.route("/about")
def about():
	return render_template("ABOUT.html")

@app.route("/add_students",methods = ["GET","POST"])
def add_students():
	form = AddStudent()
	if form.validate_on_submit():
		flash('Student added successfully', 'success')
	return render_template("add_students.html",form = form)

@app.route("/remove_students",methods = ["GET","POST"])
def remove_students():
	form = RemoveStudent()
	if form.validate_on_submit():
		flash('Student removed successfully', 'success')
	return render_template("remove_students.html",form = form)

@app.route("/edit_students_details",methods = ["GET","POST"])
def edit_students_details():
	form = EditStudentDetails()
	if form.validate_on_submit():
		flash('Student details changed successfully', 'success')
	return render_template("edit_students_details.html",form = form)


if __name__ == '__main__':
	app.run(debug = True)