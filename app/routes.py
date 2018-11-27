from flask import render_template, make_response
from app import app
import pdfkit

@app.route('/pdf')
def pdf():
  fo=open("app/head.txt","r")
  text=fo.read()
  fo.close()
  fo=open("app/write.txt","w+")
  fo.write('\t\t\t\t\t\t\t\t\t\t\t'+text)
  fo.close()
  fo=open("app/body.txt","r")
  text1=fo.read()
  fo.close()
  fo=open("app/write.txt","a+")
  fo.write('\n\n\t'+text1)
  fo.close()
  rendered = render_template('pdf.html')
  txt = ['write.txt']
  pdf = pdfkit.from_string(rendered, False)
  response = make_response(pdf)
  response.headers['Content-Type'] = 'application/pdf'
  response.headers['Content-Disposition'] = 'inline; filename=cars.pdf'
  return response

if __name__=="__main__":
   app.run(debug=True)
