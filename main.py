from flask import Flask, render_template, send_from_directory, url_for

from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

app =Flask(__name__)
app.config['SECRET_KEY'] ='asldfklj'
app.config['UPLOAD_PHOTOS_DEST'] ='uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploasForm(FlaskForm):
    photo =FileField(
        ValueError =[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File filed should not be empty')
        ]
    )
    submit =SubmitField('Upload')
    
@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PHOTOS_DEST'], filename)

@app.route('/',methods =['GET','POST'])
def upload_image():
    form =UploasForm()
    if form.validate_on_submit():
        filename =photos.save(form.photo.data)
        file_url =url_for('get_file', filename =filename)
    else:
        file_url =None
    return render_template('index.html', form =form, file_url =file_url)

if __name__ == '__main__':
    app.run(debug=True)