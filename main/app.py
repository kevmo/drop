from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = 1

db = SQLAlchemy(app)


# View/handler to drop all the images
@app.route('/', methods=)
def index():
    return render_template('index.html')

# Handler to

app.run()