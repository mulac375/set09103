from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


posts = [

    {   
        'Band': 'Oasis',
        'album': 'Definitely Maybe',
        'Content': 'First post content',
        'date_posted': 'October 28/10/2018'
    },
    {
         'Band': 'Oasis',
        'album': 'Whats the Story',
        'Content': 'Second  post content',
        'date_posted': 'October 28/10/2018'
     }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts), 200

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact/", methods=['GET', 'POST'])
def account():
    return render_template('contact.html')
  
@ app.route("/albums")
def albums():
    return render_template('albums.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if  __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)

