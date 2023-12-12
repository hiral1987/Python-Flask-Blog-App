from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Integer, String
# from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import json
from flask_mail import Mail, Message
import os
from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
import math

mail = Mail()

with open('config.json', 'r') as f:
    params = json.load(f)['params']

app = Flask(__name__)
app.secret_key = 'dsfgglglgmlgm45iky'
app.config['UPLOAD_LOCATION'] = params['upload_loc']
mail.init_app(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIl_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
)
local_server = params['local_sever']
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db = SQLAlchemy(app)


class Contact(db.Model):
    # srno: Mapped[int] = mapped_column(Integer, primary_key=True)
    # email: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    # mobile_no: Mapped[str] = mapped_column(String)
    # message: Mapped[str] = mapped_column(String)
    # name: Mapped[str] = mapped_column(String)
    # date: Mapped[str] = mapped_column(String)
    srno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=False, nullable=False)
    mobile_no = db.Column(db.String(13), unique=False, nullable=False)
    message = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)


class Posts(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    subheading = db.Column(db.String(500), unique=False, nullable=False)
    slug = db.Column(db.String(13), unique=False, nullable=False)
    content = db.Column(db.String(80), unique=False, nullable=False)
    img_file = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)


@app.route("/")
def home():
    posts = Posts.query.filter_by().all()  # [0:params['no_of_posts']]
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    page = request.args.get('page')

    total_page = int(params['no_of_posts'])

    if not str(page).isnumeric():
        page = 1
    else:
        page = int(page)

    posts = posts[((page - 1) * total_page): (((page - 1) * total_page) + total_page)]

    if page == 1:
        prev = '#'
        nextp = '/?page=' + str(page + 1)
    elif page == last:
        prev = '/?page=' + str(page - 1)
        nextp = '#'
    else:
        prev = '/?page=' + str(page - 1)
        nextp = '/?page=' + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=nextp)


@app.route("/dashboard")
def dashboard():
    # return "<p>Hello, World!</p>"
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.filter_by().all()
        return render_template('dashboard.html', params=params, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.filter_by().all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == params['admin_user'] and password == params['admin_password']:
            session['user'] = username
            posts = Posts.query.filter_by().all()
            return render_template('dashboard.html', params=params, posts=posts)

    else:
        return render_template('sign_in.html', params=params)


@app.route("/about")
def about():
    # return "<p>This is demo web app</p>"
    return render_template('about.html', params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        print(name, email, phone, message)
        # name = request.form.get('')

        entry = Contact(name=name, email=email, mobile_no=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()

        # mail.send_message(
        #     "New message from Blog",
        #     sender=email,
        #     recipients=['hiral.dharod1987@gmail.com'],
        #     body=f'Dear {name},\n\n{message}\n\n{phone}'
        # )
        msg = Message("New message from Blog",
                      sender=email,
                      recipients=['hiral.dharod1987@gmail.com'])
        mail.send(msg)
    # return "<p>This is demo web app</p>"
    return render_template('contact.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    # return "<p>This is demo web app</p>"

    posts = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params=params, post=posts)


@app.route("/edit/<string:srno>", methods=['GET', 'POST'])
def edit(srno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            tagline = request.form.get('tagline')
            content = request.form.get('content')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if srno == '0':
                post1 = Posts(title=title, subheading=tagline, content=content, slug=slug, img_file=img_file, date=date)
                db.session.add(post1)
                db.session.commit()
            else:
                post1 = Posts.query.filter_by(srno=srno).first()
                post1.title = title
                post1.subheading = tagline
                post1.content = content
                post1.slug = slug
                post1.img_file = img_file
                post1.date = date
                db.session.commit()
                redirect('/edit/' + srno)
        post1 = Posts.query.filter_by(srno=srno).first()
        return render_template('edit.html', params=params, post=post1)


@app.route("/delete/<string:srno>", methods=['GET', 'POST'])
def delete(srno):
    if 'user' in session and session['user'] == params['admin_user']:
        p = Posts.query.filter_by(srno=srno).first()
        db.session.delete(p)
        db.session.commit()

    posts = Posts.query.filter_by().all()
    return render_template('dashboard.html', params=params, posts=posts)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            file = request.files['upload']
            file.save(os.path.join(app.config['UPLOAD_LOCATION'], secure_filename(file.filename)))
            return 'Uploaded successfully'


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/login')


app.run(debug=True)
