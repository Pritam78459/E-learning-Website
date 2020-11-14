from flask import render_template, flash, redirect,url_for
from LMS_website import app
from LMS_website.database_models import Student_identity_details, Teacher_identity_details, Subject_details, Organization_details, SubjectContents 
from LMS_website.forms import StudentLogin, TeacherLogin, OrganizationLogin, OrganizationRegister, AddStaff, EditStaffDetails, RemoveStaff, AddStudent, RemoveStudent, MakeClasses, EditStudentDetails

# routes for all the pages

#main page
@app.route("/")
@app.route("/main")
def main():
	background_image = url_for('static',filename = "images/" + "23460.jpg")
	return render_template("main.html",image_file = background_image)


# ------ login section ------
# student login
@app.route("/student_login",methods = ["GET","POST"])
def student_login():

	form = StudentLogin()
	if form.validate_on_submit():
		if form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('student_browse_catalouge'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("Student_login.html",form = form, image_file = background_image)

#teacher login
@app.route("/teacher_login",methods = ["GET","POST"])
def teacher_login():

	form  = TeacherLogin()
	if form.validate_on_submit():
		if form.password.data == 'password':
		    flash('You have been logged in!', 'success')
		    return redirect(url_for('teacher_browse_catalouge'))
		else:
		    flash('Login Unsuccessful. Please check username and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("teacher_login.html",form = form,image_file = background_image)

#organization login
@app.route("/organization_login",methods = ["GET","POST"])
def organization_login():

	form  = OrganizationLogin()
	if form.validate_on_submit():
		if form.password.data == 'password':
		    flash('You have been logged in!', 'success')
		    return redirect(url_for('organization'))
		else:
		    flash('Login Unsuccessful. Please check username and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("organization_login.html",form = form,image_file = background_image)

#organization register
@app.route("/organization_register",methods = ["GET","POST"])
def organization_register():

	form  = OrganizationRegister()
	if form.validate_on_submit():
		flash('Your account has been created!', 'success')
		return redirect(url_for('organization_login'))
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("organization_register.html",form = form,image_file = background_image)


# ------ student section ------ 
# main catalouge
@app.route("/student_browse_catalouge")
def student_browse_catalouge():
	return render_template("student_browse_catalouge.html")

# grade page
@app.route("/grade")
def grade():
	return render_template("grade.html")

#course details pages
@app.route("/course_details")
def course_details():
	return render_template("course_details.html")

#student details
@app.route("/student_details")
def student_details():
	return render_template("index.html")

# ------ teacher section ------ 
# teacher's catalouge
@app.route("/teacher_browse_catalouge")
def teacher_browse_catalouge():
	return render_template("teacher_browse_catalouge.html")

# teacher's details
@app.route("/teacher_details")
def teacher_details():
	return render_template("teacher_details.html")

# student enrollement page
@app.route("/add_students",methods = ["GET","POST"])
def add_students():
	form = AddStudent()
	if form.validate_on_submit():
		flash('Student added successfully', 'success')
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("add_students.html",form = form,image_file = background_image)

# removing student's page
@app.route("/remove_students",methods = ["GET","POST"])
def remove_students():
	form = RemoveStudent()
	if form.validate_on_submit():
		flash('Student removed successfully', 'success')
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("remove_students.html",form = form,image_file = background_image)

# editing students details page
@app.route("/edit_students_details",methods = ["GET","POST"])
def edit_students_details():
	form = EditStudentDetails()
	if form.validate_on_submit():
		flash('Student details changed successfully', 'success')
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("edit_students_details.html",form = form,image_file = background_image)


# ------ organization section ------
# organizatation home page
@app.route("/organization")
def organization():
	background_image = url_for('static',filename = "images/" + "organization.jpg")
	return render_template("organization.html", image_file = background_image)

# adding staff page
@app.route("/add_staff",methods = ["GET","POST"])
def add_staff():
	form = AddStaff()
	if form.validate_on_submit():
		flash('Teacher added successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("add_staff.html",form = form, image_file = background_image)

# editing staff page
@app.route("/edit_staff")
def edit_staff():
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("edit_staff.html", image_file = background_image)

# editing staff details page
@app.route("/edit_staff_details",methods = ["GET","POST"])
def edit_staff_details():
	form = EditStaffDetails()
	if form.validate_on_submit():
		flash('Teacher details changed successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("edit_staff_details.html",form = form, image_file = background_image)

# making classes page
@app.route("/make_classes",methods = ["GET","POST"])
def make_classes():
	form = MakeClasses()
	if form.validate_on_submit():
		flash('Subject added successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization2.jpg")
	return render_template("make_classes.html",form = form,image_file = background_image)

# removing staff page
@app.route("/remove_staff",methods = ["GET","POST"])
def remove_staff():
	form = RemoveStaff()
	if form.validate_on_submit():
		flash('Teacher remove successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("remove_staff.html",form = form,image_file = background_image)



# ------ other pages ------
# about us page
@app.route("/about")
def about():
	return render_template("ABOUT.html")