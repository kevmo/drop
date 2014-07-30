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
im = pyimgur.Imgur('')
image = im.get_image('S1jmapR')
print(image.title) # Cat Ying & Yang
print(image.link) # http://imgur.com/S1jmapR.jpg


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


# View/handler to drop all the images
@app.route('/', methods=['GET', 'POST'])
def index():
    print "request method: %s" % request.method
    if request.method == 'POST':
        # print "data: ", type(request.data)
        # print "content-type: %r" % request.content_type
        if request.files:
            image = Image(image='SUP')
            db.session.add(image)
            db.session.commit()
            print "saved"
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
