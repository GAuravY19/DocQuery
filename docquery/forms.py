from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired

class DocUploadForm(FlaskForm):
    doc = FileField("Please upload a PDF to get started.", validators=[                                                                       FileAllowed(["pdf"])])
    submit = SubmitField("Submit")
