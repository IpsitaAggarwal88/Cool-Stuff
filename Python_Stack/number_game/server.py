from flask import Flask, render_template, redirect, session, request
import random
app=Flask(__name__)
app.secret_key='MySecret'

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/', methods=['POST'])
def new():
	if(session.get('number1')==None):
		session['number1']=random.randint(1,100)
		print session['number1']
	guess=int(request.form['number'])
	if(guess>session['number1']):
		string="Too High"
	elif(guess<session['number1']):
		string="Too Low"
	elif(guess==session['number1']):
		string="Right Guess"
		session.pop('number1')


	return render_template('index.html',string1=string)
app.run(debug=True)