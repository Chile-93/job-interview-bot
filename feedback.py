import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_answers(job_type, interview_level, questions, answers):
    """
    Given a list of questions and user answers, return AI-generated feedback.
    """

    # Build a formatted string to send to GPT
    prompt = f"""
    You are an expert job interviewer for a {job_type} role and {interview_level}.

    The candidate has answered 4 interview questions depending on the interview_level. 
    For each question answer, give a well constructed feedback and score, 
    every quesntion feedback should be returned in a new line.
    
    Keep the feedback simple and helpful, feedback for each answered question should be in different pargraphs with two line spacing after every feedback, put the result in numbered format, 
    also give the user an over all interview score in percentage according to users performance 

    Here are the responses:
    """

    for i in range(len(questions)):
        prompt += f"\n\nQ{i+1}: {questions[i]}\nA{i+1}: {answers[i]}"

    # Call OpenAI for feedback
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional career coach and job interviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract feedback from the response
    feedback = response['choices'][0]['message']['content']
    return feedback
