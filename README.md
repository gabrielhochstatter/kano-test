# Kano Test

Technical test for Kano.

Tech used:
- Python (Flask)
- Bootstrap for basic styling and the navbar
- Wtforms for the forms

### How to run:

- Clone this repo
- Navigate to the folder in your command line
- Make sure the dependencies `flask` and `flask-wtf` are installed
- Enter `$ flask run` or alternatively `$ python3 app.py`
- The site should be running on `localhost:5000`

- Alternatively if you have Docker installed, you can run `docker-compose up` and the app will start on `localhost:5000`. The only caveat here is that the `message_log.txt` file will not save in the project directory, however the POST request is still handled correctly it seems.

### Notes:

- The form saves the inputs into a file called `message_log.txt` in the root directory of the project. If that file doesn't exist it will be created. This is instead of saving it to a database, but the principle is quite similar (minus creating a model for the messages).
- Also for some reason I couldn't manage to override the bootstrap css with custom css, so the color scheme is still stuck on the basic bootstrap one. This might be because I'm not using the `flask-bootstrap` extension, which I only discovered once I'd built the whole site.
