from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index/')
def index():
	"""
	This method is a controller. a method is function with side-effects. python just has methods.
	"""
	return render_template('index.jade')

@app.route('/about/')
def about():
	return render_template('about.jade')
	
""" for academic contributors"""
@app.route('/contribute/')
def contribute():
	return render_template('contribute.jade')
	
""" contact information """
@app.route('/contact/')
def contact():
	return render_template('contact.jade')

""" audio-doc 1 (science)"""
@app.route('/ad1/')
def ad1():
	return render_template('ad1.jade')
	
""" audio-doc 2 (humanities) """
@app.route('/ad2/')
def ad2():
	return render_template('ad2.jade')

'''@app.route('/test/')
def test():
		return render_template('test')
	'''
""" comment box for user feedback"""
@app.route('/comment/', methods=['POST'])
def comment():
	print("@@@@@@@@@@@@@@@@@@")
	print(request.form)

"""
the route /login is a POST method. this means that it only accepts posts. (ie: you can't
GET it from typing it in the URL)
"""

'''
@app.route('/login', method=["POST"])
def login():
	"""
	params is a dictionary: allows you to access the request parameters. note: params might not 
	be the right command.
	"""
	email = params["email"]  
'''
