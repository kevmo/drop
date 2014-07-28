from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from core import Service


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['DEBUG'] = 1

db = SQLAlchemy(app)

class Image(db.Model):
    __tablename__ = 'files'

    id = db.Column('id', db.Integer, primary_key=True)
    file = db.Column('file', db.BLOB)

    def __repr__(self):
        return '<file %r>' % self.id


class Images_Service(Service):
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
            print "files: %r" % request.files['file1']
            try:
                Images_Service.create(

                )
        return redirect('/view')
    return render_template('index.html')

# Handler to
@app.route('/view')
def see_file():
    return 'haaaay'


if __name__ == '__main__':
    app.run()