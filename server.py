from flask import Flask, render_template, request,flash,redirect,session
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key="ThisisSecret"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'] )
def process():
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	session['number'] = request.form['number']
	session['location'] = request.form['location']

	errors = False

	if len(request.form['name']) < 1:
		flash("Name can not be empty")
		errors = True

	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is incorrect")
		errors = True

	if len(request.form['number']) < 1:
		flash("Please add a phone number")
		errors = True
	if len(request.form['location']) < 1:
		flash("please select a location")
		errors = True
	
	if errors:
		return redirect('/')
	else:
		return render_template('process.html')

app.run(debug=True)	
