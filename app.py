from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/cardetails'
db.init_app(app)

from models import User

@app.route('/', methods=['GET', 'POST'])
def main1():
	return render_template('index.html')

@app.route('/index')
def index():
	carvars=User.query.all()
	return render_template('add.html',carvars=carvars)

@app.route('/post_user', methods=['POST'])
def post_user():
	user= User(request.form['carbrand'], request.form['carmodel'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('main1'))

if __name__=="__main__":
	app.run(debug=True)
