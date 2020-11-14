from LMS_website import db
from datetime import datetime


class Student_identity_details(db.Model):
	student_id = db.Column(db.String(20),primary_key = True)
	student_name = db.Column(db.String(50),unique = True,nullable = False)
	student_password = db.Column(db.String(30),nullable=False)
	student_email = db.Column(db.String(40),nullable = False)
	subjects = db.relationship('Subject_details')

	def __repr__(self):
		return f"Student:'{self.student_id}','{self.student_name}'"

class Teacher_identity_details(db.Model):
	teacher_id = db.Column(db.String(20),primary_key = True)
	teacher_name = db.Column(db.String(50),unique = True,nullable = False)
	teacher_password = db.Column(db.String(30),nullable=False)
	teacher_email = db.Column(db.String(40),nullable = False)
	posts = db.relationship('SubjectContents')
	subjects = db.relationship('Subject_details')

	def __repr__(self):
		return f"Teacher:'{self.teacher_id}','{self.teacher_name}'"

class Subject_details(db.Model):
	subject_id = db.Column(db.String(20),primary_key = True)
	subject_name = db.Column(db.String(40),nullable=False)
	student_enrolled = db.Column(db.String(40),db.ForeignKey('student_identity_details.student_id'),nullable=False)
	teacher_assigned = db.Column(db.String(40),db.ForeignKey('teacher_identity_details.teacher_id'),nullable=False)

	def __repr__(self):
		return f"Subject:'{self.subject_name}','{self.teacher_assigned}'"

class Organization_details(db.Model):
	organization_id = db.Column(db.String(20),primary_key = True)
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
	teacher_posted = db.Column(db.Integer, db.ForeignKey('teacher_identity_details.teacher_id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"