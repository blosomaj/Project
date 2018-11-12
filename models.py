from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

"""define your model classes here after"""

class User(db.Model):
	__tablename__ = 'users'	
	
	carid= db.Column(db.Integer, primary_key= True)
	carbrand= db.Column(db.String(80))	
	carmodel= db.Column(db.String(80))

	def __init__(self, carbrand, carmodel):
		self.carbrand= carbrand
		self.carmodel= carmodel

	def __repr__(self):
		return '<id {}>'.format(self.carid)



