from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from image import images


app = Flask(__name__)
app.config['DEBUG'] = 1

db = SQLAlchemy(app)

# View/handler to drop all the images
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/view')
    return render_template('index.html')

# Handler to
@app.route('/view')
def see_file():
    return 'haaaay'

app.run()