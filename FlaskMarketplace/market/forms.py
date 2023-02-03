from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market import mongo

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        db = mongo['DbUsers']
        collection= db['users']
        print(username_to_check)
        userdict= collection.find({"username":str(username_to_check.data)})
        userlst=[]
        for i in userdict:
            print(i)
            userlst.append(i)
        print(userlst)
        if(len(userlst)==0):
            print("User Not there")
        else:
            print("User Is Present")  
            raise ValidationError('Username is already exists! Please try a different User Name.')   

    def validate_emailaddress(self, address_to_check):
        db= mongo['DbUsers']
        collection= db['users']
        userdict= collection.find({"email":str(address_to_check.data)})
        userlst=[]
        for i in userdict:
            userlst.append(i)

        if(len(userlst)==0):
            print("User Not there")
        else:
            print("User Is Present")  
            raise ValidationError('Email Address is already exists! Please try a different email.')  


    username = StringField(label ='User Name', validators=[Length(min =2, max=30), DataRequired()])
    email_id = StringField(label= 'Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label= 'Create Account')   
    
class LogInForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Passowrd', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
    
