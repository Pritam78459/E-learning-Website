from LMS_website import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user_organization(user_id):
	if Organization_details.query.get(user_id):
		return Organization_details.query.get(user_id)
	elif Student_identity_details.query.get(user_id):
		return Student_identity_details.query.get(user_id)
	elif Teacher_identity_details.query.get(user_id):
		return Teacher_identity_details.query.get(user_id)

#@login_manager.user_loader
#def load_user_student(user_id):
#	return Student_identity_details.query.get(user_id)

#@login_manager.user_loader
#def load_user_teacher(user_id):
#	return Teacher_identity_details.query.get(user_id)


class Student_identity_details(db.Model,UserMixin):
	id = db.Column(db.String(20),primary_key = True)
	student_name = db.Column(db.String(50),unique = True,nullable = False)
	student_password = db.Column(db.String(30),nullable=False)
	student_email = db.Column(db.String(40),nullable = False)
	subjects = db.relationship('Subject_details')

	def __repr__(self):
		return f"Student:'{self.id}','{self.student_name}'"

class Teacher_identity_details(db.Model,UserMixin):
	id = db.Column(db.String(20),primary_key = True)
	teacher_name = db.Column(db.String(50),unique = True,nullable = False)
	teacher_password = db.Column(db.String(30),nullable=False)
	teacher_email = db.Column(db.String(40),nullable = False)
	posts = db.relationship('SubjectContents')
	subjects = db.relationship('Subject_details')


	def __repr__(self):
		return f"Teacher:'{self.id}','{self.teacher_name}'"

class Subject_details(db.Model):
	subject_id = db.Column(db.String(20),primary_key = True)
	subject_name = db.Column(db.String(40),nullable=False)
	student_enrolled = db.Column(db.String(40),db.ForeignKey('student_identity_details.id'),nullable=False)
	teacher_assigned = db.Column(db.String(40),db.ForeignKey('teacher_identity_details.id'),nullable=False)

	def __repr__(self):
		return f"Subject:'{self.subject_name}','{self.teacher_assigned}'"

class Organization_details(db.Model,UserMixin):
	id = db.Column(db.String(20),primary_key = True)
	organization_name = db.Column(db.String(50),unique = True,nullable = False)
	organization_password = db.Column(db.String(30),nullable=False)
	organization_email = db.Column(db.String(40),nullable = False)


	def __repr__(self):
		return f"Organization:'{self.organization_id}'"

class SubjectContents(db.Model):
	notes_id = db.Column(db.String(20),primary_key = True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	teacher_posted = db.Column(db.Integer, db.ForeignKey('teacher_identity_details.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"