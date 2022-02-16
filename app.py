import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from azure.storage.blob import BlobServiceClient

from models import db, User, Pin
import storage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
db.create_all(app=app)

@app.route('/')
def index():
   print('Request for index page received')
   images = list(reversed(Pin.query.all()))
   return render_template('index.html', images=images)


@app.route('/newimage', methods=['POST'])
def post_image():
    #nickname = current_user.nickname
    image_url = request.form.get('image_url')
    image_text = request.form.get('image_text')

    if image_url and image_text:
        new_pin = Pin(text=image_text, image=image_url)
        db.session.add(new_pin)
        db.session.commit()
        return render_template('newpin.html', new_pin = new_pin)
    else:
        return redirect(url_for('index'))

@app.route("/upload")
def photos():
   images = storage.get_blob_items()
   return render_template('upload.html', images=images)


#flask endpoint to upload a photo
@app.route("/upload-photos", methods=["POST"])
def upload_photos():
    filenames = ""

    for file in request.files.getlist("photos"):
        try:
            storage.upload_blob(file) # upload the file to the container using the filename as the blob name
            filenames += file.filename + "<br /> "
        except Exception as e:
            print(e)
            print("Ignoring duplicate filenames") # ignore duplicate filenames
        
    return redirect('/upload')

if __name__ == '__main__':
   app.run()