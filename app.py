from flask import Flask, render_template, flash, request
from forms import ContactForm
from save_file import save_to_file
app = Flask(__name__)

app.config['SECRET_KEY'] = '844a137b7edbb5e5dec075380a52e2d0'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        save_to_file('message_log.txt', request.form['email'], request.form['name'], request.form['message'])
        flash('Your message was sent!', 'success')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)