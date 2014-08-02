import os

import pyimgur
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from sqlalchemy.dialects import postgresql
from sqlalchemy import BLOB
from werkzeug.utils import secure_filename

from core import Service

CLIENT_ID = "Your_applications_client_id"
im = pyimgur.Imgur('b467811fb9e6bb9')
# image = im.get_image('S1jmapR')
# print(image.title) # Cat Ying & Yang
# print(image.link) # http://imgur.com/S1jmapR.jpg


# create and configure app
app = Flask(__name__)
app.config['DEBUG'] = 1
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'postgresql+psycopg2://hoth@localhost:5432/drop'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# instantiate extensions
db = SQLAlchemy(app)
manager = Manager(app)

# define model and table
class Image(db.Model):
    __tablename__ = 'files'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    image = db.Column('image', db.String(100))

    def __repr__(self):
        return '<file %r>' % self.id


# put SQL services on top of model
class ImagesService(Service):
    __model__ = Image

#instantiate service
images = ImagesService()


# View/handler to drop all the images
@app.route('/', methods=['GET', 'POST'])
def index():
    print "request method: %s" % request.method
    if request.method == 'POST':
        # print "data: ", type(request.data)
        # print "content-type: %r" % request.content_type
        if request.files:
            images.create(image='BETH BETH BETH')
            print images.does_this_work()
            # db.session.add(image)
            # db.session.commit()
            # print "saved"

            file1 = request.files['file1']
            print "FIRE FILE1",  file1.name
            #is there a stream here?
            print "STREAM: \n", file1.stream

            try:
                # im = pyimgur.Imgur('b467811fb9e6bb9')
                print im.upload_image(
                    path="./gucci.jpg"
                )
                print "yasss"
                # uploaded_image = im.upload_image(
                #     path='http://i.imgur.com/UGcKkRe.png')
                # print "YASSS"
                # print(uploaded_image.title)
                # print(uploaded_image.date)
            except:
                print "Imgur upload is a nope"

        # and ImagesService.create:
        #
        #     new_file = request.files['file1']
        #     try:
        #         ImagesService.create(
        #             image="hi"
        #         )
        #     except:
        #         print "Image_Service not working"
        return redirect('/view')
    return render_template('index.html')


# Handler to
@app.route('/view')
def see_file():
    return 'haaaay'


@manager.command
def newdb():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    db.create_all()
    manager.run()
