from flask import Flask, render_template, request
from stories import story
app = Flask(__name__)
##return Words for home 
##for story im returning generate 
@app.route("/")
def home():

  return render_template("home.html" )


@app.route("/story")
def storygen(): 
  place = request.args.get('place')
  noun  = request.args.get('noun')
  verb = request.args.get('verb')
  adjective  = request.args.get('adjective')
  pn = request.args.get('plural_noun')
  answer = {"place": place, "noun": noun, "verb": verb, "adjective":adjective , "plural_noun":pn}
  showstory = story.generate(answer)
  return render_template("story.html", story = showstory)
