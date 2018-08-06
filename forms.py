from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    message = StringField('Message', validators=[DataRequired()], widget=TextArea(), render_kw={"placeholder": "Type your message here!"})
    submit = SubmitField('Submit')