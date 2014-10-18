# -*- coding: utf-8 -*-
from flask import Flask, render_template,request, flash
from forms import Params
from crawler_amazon import amazoncrawl
from crawler_asos import asoscrawl

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
      par['height'] = form.height.data
      par['weight'] = form.weight.data
      par['gender'] = form.gender.data
      par['keywords'] = form.keywords.data
      outlist = amazoncrawl(par)
      outlist = outlist + asoscrawl(par)
      return render_template('output.html', outlist=outlist)
    else:
      return 'Form posted.'
 
 
  elif request.method == 'GET':
    return render_template('params.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
