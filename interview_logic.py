import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_interview_questions(job_type):
    prompt = f"""
    Generate exactly 4 unique, intermediate-level interview questions related to the job title {job_type}.
    Do not repeat previous patterns. Make sure each question is clear and specific to the job.
    Format the questions as a numbered list, one per line.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a job interviewer who generates smart, relevant questions based on the selected job type."},
            {"role": "user", "content": prompt}
        ]
    )

    # The raw content from OpenAI
    raw_output = response['choices'][0]['message']['content'].strip()

    # DEBUG: print to check what came back
    print("RAW OPENAI RESPONSE >>>", raw_output)

    # Convert string into list of questions
    questions = [line.strip() for line in raw_output.split('\n') if line.strip()]
    
    # Optionally, trim the numbers like "1. ", "2. ", etc.
    cleaned_questions = [q.split('. ', 1)[1] if '. ' in q else q for q in questions]

    return cleaned_questions
