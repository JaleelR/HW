from flask import Flask, render_template, redirect, request, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Naruto7'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



response = []; 

@app.route('/')
def home(): 
    return render_template("home.html", title = satisfaction_survey.title, instructions = satisfaction_survey.instructions )


@app.route('/questions/<int:qid>')
def show_question(qid):
    qobj = satisfaction_survey.questions

    # Check if the question ID is out of bounds
    if qid > len(qobj):
        flash("Out of order!!!!!!")
        return redirect(url_for("show_question", qid = 1 ))  # Redirect to the first question
        
    # Check if the user hasn't answered the previous question
    if qid > 0 and qid - 1 > len(response): 
    
         # Assuming `responses` is a list storing user responses
        return redirect(url_for("show_question",  qid = qid- 1))  # Redirect to the previous question

    quest = qobj[qid].question  # Adjusting index to match 0-based indexing
    qlist = qobj[qid].choices

    return render_template("questions.html", final_question=quest, choice=qlist)


@app.route('/answer', methods = ["POST"])
def answer():
    global response
    answer = request.form.get("answer")
    if len(response) < 4: 
      next_question_index = len(response)  
      response.append(answer)
      print(response)
      return redirect( url_for("show_question", qid=next_question_index))
    else:
        response.clear()
        return redirect("/thankyou")




@app.route('/thankyou')
def thankyouu():
    return render_template("thank_you.html")

# app.route('questions/<1>')
# def question1(1):
#     question = satisfaction_survey.questions[0].question

#     return render_template("q0.html", question = question)
# app.route('questions/<2>')
# def question2(2):
#     question = satisfaction_survey.questions[0].question
#     return render_template("q0.html", question = question)

# app.route('questions/<3>')
# def question3(3):
#     question = satisfaction_survey.questions[0].question
#     return render_template("q0.html", question = question)