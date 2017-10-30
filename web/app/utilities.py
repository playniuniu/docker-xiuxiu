#!/usr/bin/env python3
import os
from werkzeug.utils import secure_filename

PHOTO_FOLDER = os.path.join(os.getcwd(), "./static/upload/")
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_photo_file(request):
    if 'photo' not in request.files:
        print("No photo upload")
        return None

    photo = request.files['photo']
    if photo.filename == "":
        return ("No photo selected")
        return None

    if photo and allowed_file(photo.filename):
        file_name = secure_filename(photo.filename)
        file_path = os.path.join(os.path.dirname(__file__),
                                 "static/upload/", file_name)
        photo.save(file_path)
        print("Save photo in {}".format(file_path))
        return file_path
