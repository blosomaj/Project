from flask import render_template, redirect, url_for, request, make_response
from app import app, db, User
from app.forms import NewForm, EditForm
import pdfkit

@app.route('/')
@app.route('/index')
def index():
  myUser = User.query.all()
  return render_template('index.html', title='Home', myUser=myUser)

@app.route('/add', methods=['GET', 'POST'])
def add():
  form=NewForm()
  if form.validate_on_submit():
    user = User(carbrand=form.carbrand.data, carmodel=form.carmodel.data) 
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('add.html',title='Add',form=form)

@app.route('/edit/<int:carid>', methods=['GET', 'POST'])
def edit(carid):
  qry= User.query.get(carid)
  form= EditForm(formdata=request.form, obj=qry)
  if form.validate_on_submit():
    car= User(carbrand=form.carbrand.data, carmodel=form.carmodel.data)
    qry.carbrand=form.carbrand.data
    qry.carmodel=form.carmodel.data    
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('edit.html',title='Edit',form=form)

@app.route('/pdf')
def pdf():
  fo=open("head.txt","r")
  text=fo.read()
  fo.close()
  fo=open("app/write.txt","w+")
  fo.write('\t\t\t\t\t\t\t\t\t\t\t'+text)
  fo.close()
  fo=open("body.txt","r")
  text1=fo.read()
  fo.close()
  fo=open("app/write.txt","a+")
  fo.write('\n\n\t'+text1)
  fo.close()
  myCars = User.query.all()
  rendered = render_template('pdf.html',myCars=myCars)
  txt = ['write.txt']
  pdf = pdfkit.from_string(rendered, False)
  response = make_response(pdf)
  response.headers['Content-Type'] = 'application/pdf'
  response.headers['Content-Disposition'] = 'inline; filename=cars.pdf'
  return response

if __name__=="__main__":
   app.run(debug=True)
		


