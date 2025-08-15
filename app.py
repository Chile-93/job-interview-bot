from flask import Flask, render_template, request
from interview_logic import generate_interview_questions  # or from interview import ...
from feedback import analyze_answers  # logic to analyze responses

app = Flask(__name__)

# Home route – show the job selection form
@app.route('/')
def index():
    return render_template("index.html")

# Route to generate interview questions
@app.route('/interview', methods=['POST'])
def interview():
    # Get the selected job type from the form
    job_type = request.form['job_type']
    interview_level = request.form['interview_level']

    # Generate interview questions based on job type
    questions = generate_interview_questions(job_type, interview_level)

    # print("QUESTIONS >>>", questions)

    # Render the interview form with questions
    return render_template("interview.html", job_type=job_type, interview_level=interview_level, questions=questions)

#Route to handle user answers and return AI feedback
@app.route('/feedback', methods=['POST'])
def feedback():
    # Get job type again
    job_type = request.form['job_type']
    interview_level = request.form['interview_level']
  

    # Retrieve all 4 questions and answers from the form
    questions = [
        request.form['question1'],
        request.form['question2'],
        request.form['question3'],
        request.form['question4']
    ]

    answers = [
        request.form['answer1'],
        request.form['answer2'],
        request.form['answer3'],
        request.form['answer4']
    ]

    # Analyze the answers using OpenAI (defined in feedback.py)
    feedback_text = analyze_answers(job_type, interview_level, questions, answers)

    # Show the result with original Q&A and AI feedback
    return render_template("result.html",
                           job_type=job_type,
                           interview_level=interview_level,
                           questions=questions,
                           answers=answers,
                           feedback=feedback_text)

# Run the Flask app

if __name__== '__main__':
   app.run(host='0.0.0.0', debug=True) #to run on other devices but on the same network connection