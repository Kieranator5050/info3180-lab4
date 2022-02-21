from email.mime import image
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    img_file = FileField('img_file', 
                            validators=[
                                FileRequired(), 
                                FileAllowed(['jpg','png'], "Only Images!" )
                                ])
