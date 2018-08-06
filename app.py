from flask import Flask, render_template
from forms import ContactForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '844a137b7edbb5e5dec075380a52e2d0'

@app.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)