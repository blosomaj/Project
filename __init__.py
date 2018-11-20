from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug=True

db = SQLAlchemy(app)
migrate = Migrate(app,db)
 
class User(db.Model):
   __tablename__= 'user'

   carid = db.Column(db.Integer, primary_key= True)
   carbrand = db.Column(db.String(80), index=True)	
   carmodel = db.Column(db.String(80), index=True)

   def __repr__(self):
       return '<Car {}>'.format(self.carbrand)

from app import routes

if __name__ == "__main__":
   app.run(debug=True)
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
