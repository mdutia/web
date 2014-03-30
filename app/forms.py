from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, RadioField, TextAreaField, SelectField, IntegerField
from wtforms.validators import Required, NumberRange

class LoginForm(Form):
    uname= TextField('username', validators = [Required()])
    pwd = PasswordField('pwd', validators = [Required()])
    #remember_me = BooleanField('remember_me', default = False)
    
class SelectGroupMemberForm (Form):
    #choicelist=[]
    #for i in range (1,n):
        #choicelist.append ( (str(n), '1') ) 
    selected= RadioField('Group members', choices= [
        ('1','     '),
        ('2','     '),
        ('3','     '),
        ('4','     '),
        ('5','     '),
        ('6','     '),
        ('7','     '),
        ('8','     '),
        ('9','     '),
        ('10','     '),
        ('11','     '),
        ('12','     '),
        ('13','     '),
        ('14','     '),
        ('15','     '),
    ] )
    
class EvaluationForm (Form):
    m1= IntegerField('Criterion 1', validators= [NumberRange(0,5,'Please give a mark between 0 - 5')])
    m2= IntegerField(label='Criterion 2', validators= [NumberRange(0,5,'Please give a mark between 0 - 5')])
    m3= IntegerField(label='Criterion 3', validators= [NumberRange(0,5,'Please give a mark between 0 - 5')])
    m4= IntegerField(label='Criterion 4', validators= [NumberRange(0,5,'Please give a mark between 0 - 5')])
    m5= IntegerField(label='Criterion 5', validators= [NumberRange(0,5,'Please give a mark between 0 - 5')])
    j1= TextAreaField('Comment1')

    