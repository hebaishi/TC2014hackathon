from flask import Flask, render_template,request, flash
from forms import Params

app = Flask(__name__)     
app.secret_key = 'development key'
 
@app.route('/',methods = ['GET', 'POST'])
def params():
  form = Params()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      flash(form.height.data)
      return render_template('params.html', form=form)
    else:
      return 'Form posted.'
 
 
  elif request.method == 'GET':
    return render_template('params.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
