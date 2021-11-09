from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#def numberCheck(form, number):
#    if (type(int(number)<1):
#        raise ValidationError('This is not a valid number!')

class CityForm(FlaskForm):
    CityName = StringField('City Name ',
                         validators=[DataRequired(), Length(min=1, max=30)])
    CityRank = StringField('City Rank ',
                           validators=[DataRequired()])
    Visited=BooleanField('Visited')
    submit=SubmitField('Submit')
