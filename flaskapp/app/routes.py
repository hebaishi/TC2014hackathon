# -*- coding: utf-8 -*-
import random
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
    if (form.weight.data is None or form.height.data is None or form.gender.data is None or form.keywords.data is None):
      flash('All fields are required.')
      print form.height.data
      print form.weight.data
      print form.gender.data
      print form.keywords.data      
      print "Error"
      return render_template('params.html', form=form)
    else:
      par = dict()
      par['height'] = form.height.data
      par['weight'] = form.weight.data
      par['gender'] = form.gender.data
      par['keywords'] = form.keywords.data
      outlist = amazoncrawl(par)
      outlist = outlist + asoscrawl(par)
      random.shuffle(outlist)
      return render_template('output.html', outlist=outlist)
  elif request.method == 'GET':
      return render_template('params.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)
