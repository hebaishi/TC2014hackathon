from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import Required

class Params(Form):
  height = IntegerField("Height (in cm)")
  weight = IntegerField("Weight")
  gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
  keywords = TextField("Keywords")
  submit = SubmitField("Send")
