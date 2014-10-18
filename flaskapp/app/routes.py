from flask import Flask, render_template,request, flash
from forms import Params
from crawler_amazon import amazoncrawl

app = Flask(__name__)     
app.secret_key = 'development key'
 
@app.route('/',methods = ['GET', 'POST'])
def params():
  form = Params()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      flash(form.height.data)
      #form.weight.data
      par = dict()
      par['height'] = 12
      par['weight'] = 12
      par['gender'] = 'Male'
      par['keywords'] = "word1 word2"
      return render_template('output.html', outlist=amazoncrawl(par))
    else:
      return 'Form posted.'
 
 
  elif request.method == 'GET':
    return render_template('params.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
