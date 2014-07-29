import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from werkzeug.utils import secure_filename

from core import Service

#
basedir = os.path.abspath(os.path.dirname(__file__))

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

    id = db.Column('id', db.Integer, primary_key=True)
    file = db.Column('file', db.String(10000))

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
        print "data: ", type(request.data)
        if request.files:
            #save
            print "multidict: %r" % request.files
            print "type of files: %r" % type(request.files['file1'])
            try:
                Images_Service.create(
                    file = request.files['file1']
                )
            except:
                print "Image_Service not working"
        return redirect('/view')
    return render_template('index.html')

@manager.command
def hello():
    print "hello"

# Handler to
@app.route('/view')
def see_file():
    return 'haaaay'


if __name__ == '__main__':
    db.create_all()
    manager.run()
    # app.run()
