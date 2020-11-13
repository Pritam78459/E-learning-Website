from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class StudentLogin(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	email = StringField("Email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Student Login")


class TeacherLogin(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2 , max = 20	)])
	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Teacher Login")


class OrganizationLogin(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2 , max = 20	)])
	email = StringField("email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	submit = SubmitField("Organization Login")


class AddStaff(FlaskForm):

	username = StringField("username",validators = [DataRequired(), Length(min = 2, max = 20	)])
	userid = StringField("userid",validators = [DataRequired(), Length(min = 2, max = 20	)])
	email = StringField("Email",validators = [DataRequired(), Email()])
	password = PasswordField("password",validators = [DataRequired()])
	confirm_password = PasswordField("confirm password",validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField("Add Staff")


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