from LMS_website import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from LMS_website.database_models import Student_identity_details, Teacher_identity_details, Subject_details, Organization_details, SubjectContents 

db.create_all()

class StudentLogin(FlaskForm):

	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Student Login")


class TeacherLogin(FlaskForm):

	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Teacher Login")


class OrganizationLogin(FlaskForm):

	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Organization Login")


class OrganizationRegister(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2 , max = 20	)])
	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	confirm_password = PasswordField("confirm_password",validators = [DataRequired(),EqualTo('password')])
	submit = SubmitField("Create Account")

	def validate_username(self, username):
		user = Organization_details.query.filter_by(organization_name=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = Organization_details.query.filter_by(organization_email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')


class AddStaff(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	userid = StringField("userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	email = StringField("Email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	confirm_password = PasswordField("confirm password",validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField("Add Staff")

	def validate_userid(self, userid):
		user = Teacher_identity_details.query.filter_by(id=userid.data).first()
		if user:
			raise ValidationError('That userid is taken. Please choose a different one.')

	def validate_email(self, email):
		user = Teacher_identity_details.query.filter_by(teacher_email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')

class RemoveStaff(FlaskForm):

	userid = StringField("userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	submit = SubmitField("Remove Staff")


class EditStaffDetails(FlaskForm):

	current_userid = StringField("current_userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	new_username = StringField("new_username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	new_email = StringField("new_Email",validators = [DataRequired(), Email()])
	new_password = PasswordField("new_password",validators = [DataRequired()])
	new_confirm_password = PasswordField("new_confirm password",validators = [DataRequired(), EqualTo('new_password')])
	submit = SubmitField("Upload Changes")


class MakeClasses(FlaskForm):

	subjectid = StringField("subjectid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	subjectname = StringField("subjectname",validators = [DataRequired(), Length(min = 2, max = 20	)])
	assigned_teacher_id = StringField("assigned_teacher_id",validators = [DataRequired(), Length(min = 2, max = 20	)])
	submit = SubmitField("Make Subjects")


class AddStudent(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	userid = StringField("userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	email = StringField("Email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	confirm_password = PasswordField("confirm password",validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField("Add Student")

	def validate_userid(self, userid):
		user = Student_identity_details.query.filter_by(id=userid.data).first()
		if user:
			raise ValidationError('That userid is taken. Please choose a different one.')

	def validate_email(self, email):
		user = Student_identity_details.query.filter_by(student_email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')


class RemoveStudent(FlaskForm):

	userid = StringField("userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	submit = SubmitField("Remove Student")

class EditStudentDetails(FlaskForm):
	current_userid = StringField("current_userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	new_username = StringField("new_username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	new_email = StringField("new_Email",validators = [DataRequired(), Email()])
	new_password = PasswordField("new_password",validators = [DataRequired()])
	new_confirm_password = PasswordField("new_confirm password",validators = [DataRequired(), EqualTo('new_password')])
	submit = SubmitField("Upload Changes")