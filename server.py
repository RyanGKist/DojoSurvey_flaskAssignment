from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'] )
def process():
	name = request.form['name']
	email = request.form['email']
	number = request.form['number']
	location = request.form['location']
	return render_template("process.html",name=name,email=email,number=number,location=location)
app.run(debug=True)	
