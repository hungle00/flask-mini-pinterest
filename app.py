from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from models import db, User, Pin
import storage

app = Flask(__name__)
# load config from the config file we created earlier 
app.config.from_object('config')

db.init_app(app)
db.create_all(app=app)

@app.route('/')
def index():
   print('Request for index page received')
   images = list(reversed(Pin.query.all()))
   return render_template('index.html', images=images)

#####  AUTHENTICATION #####
# Login Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        return redirect(url_for('index'))
    return decorated_function

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        # get the user details from the form
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # hash the password
        password = generate_password_hash(password)
        user = User(email=email, username=username, password=password)

        db.session.add(user)
        db.session.commit()

        session['user'] = username
        flash('Thanks for signing up please login')

        return redirect(url_for('index'))

    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # search the database for the User
    user = User.query.filter_by(username=username).first()

    if user:
        password_hash = user.password

        if check_password_hash(password_hash, password):
            # The hash matches the password in the database log the user in
            session['user'] = username
            flash('Login was succesfull')
    else:
        # user wasn't found in the database
        flash('Username or password is incorrect please try again', 'error')

    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')

        flash('We hope to see you again!')

    return redirect(url_for('index'))


##### CRUD PINS #####
@app.route('/newimage', methods=['POST'])
@login_required
def post_image():
    #nickname = current_user.nickname
    image_url = request.form.get('image_url')
    image_text = request.form.get('image_text')

    if image_url and image_text:
        new_pin = Pin(title=image_text, image_url=image_url)
        db.session.add(new_pin)
        db.session.commit()
        return render_template('newpin.html', new_pin = new_pin)
    else:
        return redirect(url_for('index'))


##### UPLOAD PHOTOS  ######
@app.route("/upload")
@login_required
def photos():
   images = storage.get_blob_items()
   return render_template('upload.html', images=images)

@app.route("/upload-photos", methods=["POST"])
@login_required
def upload_photos():
    filenames = ""

    for file in request.files.getlist("photos"):
        try:
            storage.upload_blob(file) # upload the file to the container using the filename as the blob name
            filenames += file.filename + "<br /> "
        except Exception as e:
            print(e)
            print("Ignoring duplicate filenames") # ignore duplicate filenames
        
    return redirect('/upload')


if __name__ == '__main__':
   app.run()
