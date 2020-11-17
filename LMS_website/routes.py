import secrets
from flask import render_template, flash, redirect,url_for, request
from LMS_website import app, db, bcrypt
from LMS_website.database_models import Student_identity_details, Teacher_identity_details, Subject_details, Organization_details, SubjectContents 
from LMS_website.forms import StudentLogin, TeacherLogin, OrganizationLogin, OrganizationRegister, AddStaff, EditStaffDetails, RemoveStaff, AddStudent, RemoveStudent, MakeClasses, EditStudentDetails, OrganizationUpdate
from flask_login import login_user, current_user, logout_user, login_required

db.create_all()


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
	if current_user.is_authenticated:
		return redirect(url_for('student_browse_catalouge'))
	form  = StudentLogin()
	if form.validate_on_submit():
		user = Student_identity_details.query.filter_by(student_email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.student_password,form.password.data):
			login_user(user,False)
			return redirect(url_for('student_browse_catalouge'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("Student_login.html",form = form, image_file = background_image)

#teacher login
@app.route("/teacher_login",methods = ["GET","POST"])
def teacher_login():
	if current_user.is_authenticated:
		return redirect(url_for('teacher_browse_catalouge'))
	form  = TeacherLogin()
	if form.validate_on_submit():
		user = Teacher_identity_details.query.filter_by(teacher_email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.teacher_password,form.password.data):
			login_user(user,False)
			return redirect(url_for('teacher_browse_catalouge'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("teacher_login.html",form = form,image_file = background_image)

#organization login
@app.route("/organization_login",methods = ["GET","POST"])
def organization_login():
	if current_user.is_authenticated:
		return redirect(url_for('organization'))
	form  = OrganizationLogin()
	if form.validate_on_submit():
		user = Organization_details.query.filter_by(organization_email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.organization_password,form.password.data):
			login_user(user,False)
			return redirect(url_for('organization'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("organization_login.html",form = form,image_file = background_image)

#organization register
@app.route("/organization_register",methods = ["GET","POST"])
def organization_register():
	if current_user.is_authenticated:
		return redirect(url_for('organization'))
	form  = OrganizationRegister()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		account = Organization_details(id = secrets.token_hex(7),organization_name = form.username.data,organization_password = hashed_password,organization_email = form.email.data)
		db.session.add(account)
		db.session.commit()
		flash(f'Your account has been created for {form.username.data}!, you can now log in with this account', 'success')
		return redirect(url_for('organization_login'))
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("organization_register.html",form = form,image_file = background_image)


# ------ student section ------ 
# main catalouge
@app.route("/student_browse_catalouge")
@login_required
def student_browse_catalouge():
	return render_template("student_browse_catalouge.html")

# grade page
@app.route("/grade")
@login_required
def grade():
	return render_template("grade.html")

#course details pages
@app.route("/course_details")
@login_required
def course_details():
	return render_template("course_details.html")

#student details
@app.route("/student_details")
@login_required
def student_details():
	return render_template("index.html")

# ------ teacher section ------ 
# teacher's catalouge
@app.route("/teacher_browse_catalouge")
@login_required
def teacher_browse_catalouge():
	return render_template("teacher_browse_catalouge.html")

# teacher's details
@app.route("/teacher_details")
@login_required
def teacher_details():
	return render_template("teacher_details.html")

# student enrollement page
@app.route("/add_students",methods = ["GET","POST"])
@login_required
def add_students():
	form = AddStudent()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		account = Student_identity_details(id = form.userid.data,student_name = form.username.data,student_password = hashed_password,student_email = form.email.data)
		db.session.add(account)
		db.session.commit()
		flash(f'Account has been created for {form.username.data}!, you can now log in with this account', 'success')
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("add_students.html",form = form,image_file = background_image)

# removing student's page
@app.route("/remove_students",methods = ["GET","POST"])
@login_required
def remove_students():
	form = RemoveStudent()
	if form.validate_on_submit():
		flash('Student removed successfully', 'success')
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("remove_students.html",form = form,image_file = background_image)

# editing students details page
@app.route("/edit_students_details",methods = ["GET","POST"])
@login_required
def edit_students_details():
	form = EditStudentDetails()
	if form.validate_on_submit():
		student = Student_identity_details.query.filter_by(id = form.current_user_id.data ).first()
		student.student_name = form.new_username.data
		student.student_email = form.new_email.data
		db.session.commit()
		flash(f'Student account has been updated!', 'success')
		return redirect(url_for('edit_students_details'))
	background_image = url_for('static',filename = "images/" + "students.jpeg")
	return render_template("edit_students_details.html",form = form,image_file = background_image)


# ------ organization section ------
# organization home page
@app.route("/organization")
@login_required
def organization():
	background_image = url_for('static',filename = "images/" + "organization.jpg")
	return render_template("organization.html", image_file = background_image)

# adding staff page
@app.route("/add_staff",methods = ["GET","POST"])
@login_required
def add_staff():
	form = AddStaff()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		account = Teacher_identity_details(id = form.userid.data,teacher_name = form.username.data,teacher_password = hashed_password,teacher_email = form.email.data)
		db.session.add(account)
		db.session.commit()
		flash(f'Account has been created for {form.username.data}!, you can now log in with this account', 'success')
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("add_staff.html",form = form, image_file = background_image)

# editing staff page
@app.route("/edit_staff")
@login_required
def edit_staff():
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("edit_staff.html", image_file = background_image)

# editing staff details page
@app.route("/edit_staff_details",methods = ["GET","POST"])
@login_required
def edit_staff_details():
	form = EditStaffDetails()
	if form.validate_on_submit():
		teacher = Teacher_identity_details.query.filter_by(id = form.current_user_id.data ).first()
		teacher.teacher_name = form.new_username.data
		teacher.teacher_email = form.new_email.data
		db.session.commit()
		flash(f'Teacher account has been updated!', 'success')
		return redirect(url_for('edit_staff_details'))
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("edit_staff_details.html",form = form, image_file = background_image)

# making classes page
@app.route("/make_classes",methods = ["GET","POST"])
@login_required
def make_classes():
	form = MakeClasses()
	if form.validate_on_submit():
		flash('Subject added successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization2.jpg")
	return render_template("make_classes.html",form = form,image_file = background_image)

# removing staff page
@app.route("/remove_staff",methods = ["GET","POST"])
@login_required
def remove_staff():
	form = RemoveStaff()
	if form.validate_on_submit():
		flash('Teacher remove successfully', 'success')
	background_image = url_for('static',filename = "images/" + "organization3.jpg")
	return render_template("remove_staff.html",form = form,image_file = background_image)

# organization account
@app.route("/organization_account")
@login_required
def organization_account():
	return render_template("organization_account.html")

@app.route("/organization_update",methods = ["GET","POST"])
def organization_update():
	form  = OrganizationUpdate()
	if form.validate_on_submit():
		current_user.organization_name = form.username.data
		current_user.organization_email = form.email.data
		db.session.commit()
		flash(f'Your account has been updated!', 'success')
		return redirect(url_for('organization_update'))
	elif request.method == 'GET':
		form.username.data = current_user.organization_name
		form.email.data = current_user.organization_email
	background_image = url_for('static',filename = "images/" + "23467.jpg")
	return render_template("organization_update.html",form = form,image_file = background_image)



# ------ logout pages ------
# organization logout
@app.route("/organization_logout")
def organization_logout():
	logout_user()
	return redirect(url_for('organization_login'))

# teacher logout
@app.route("/teacher_logout")
def teacher_logout():
	logout_user()
	return redirect(url_for('teacher_login'))

# student logout
@app.route("/student_logout")
def student_logout():
	logout_user()
	return redirect(url_for('student_login'))

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('main'))



# ------ other pages ------
# about us page
@app.route("/about")
def about():
	return render_template("ABOUT.html")

