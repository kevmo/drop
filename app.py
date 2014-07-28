from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# from image import images


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['DEBUG'] = 1

db = SQLAlchemy(app)

# View/handler to drop all the images
@app.route('/', methods=['GET', 'POST'])
def index():
    print "request method: %s" % request.method
    if request.method == 'POST':
        print "data: ", type(request.data)
        if request.files:
            print "files: %r" % request.files
        return redirect('/view')
    return render_template('index.html')

# Handler to
@app.route('/view')
def see_file():
    return 'haaaay'

app.run()