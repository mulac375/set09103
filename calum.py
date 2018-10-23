from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html'), 200

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/albums")
def albums():
    return render_template('albums.html')

@app.route('/inherits/')
def inherits():
    return render_template('base.htm')

@app.route('/inherits/one/')
def inherits_one():
    return render_template('inherits1.html')

@app.route('/inherits/two/')
def inherits_two():
    return render_template('inherits2.html')

if  __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)

