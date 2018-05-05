from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key='MySecret'

@app.route('/')
def index():
	if(not(session.get('money_total'))):
		session['money_total']=0
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money_total():
	if(not(session.get('money'))):
		session['money']=0

	if(not(session.get('string'))):
		session['string']=""
	
	if (request.form['building']=='farm'):
		session['money']=random.randint(10,20)
		session['money_total']+=session['money']
		print session['money_total']
		session['string']+="\n Earned"+str(session['money'])+" golds from the farm!"
		print session['string']
	if(request.form['building']=='cave'):
		session['money']=random.randint(5,10)
		session['money_total']+=session['money']
		session['string']+="\n Earned"+str(session['money'])+" golds from the cave!"
	
	if(request.form['building']=='house'):
		session['money']=random.randint(2,5)
		session['money_total']+=session['money']
		session['string']+="\n Earned"+str(session['money'])+" golds from the house!"
	
	if(request.form.get('building')=='casino'):
		session['money']=random.randint(-50,50)
		session['money_total']+=session['money']
		if(session['money']<0):
			session['string']+="\n Lost"+str(session['money'])+" golds at the casino!!!"
		else:
			session['money1']=abs(session['money'])
     		session['string']+="\n Earned"+str(session['money1'])+" golds at the casino!!!"
	
	return redirect('/')
app.run(debug=True)

#session variable is printing even before it is created
#we can submit only one form at a time?
#session['string']and ['money_total']: input tag is not required.