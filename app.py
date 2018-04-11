from flask import Flask, render_template
from data import get_posts

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return render_template('blog.html', posts=get_posts())

@app.route('/blogpost/<string:id>/')
def blogpost(id):
	return render_template('blogpost.html', posts=get_posts(), id=id)

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)