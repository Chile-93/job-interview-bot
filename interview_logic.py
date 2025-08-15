import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_interview_questions(job_type, interview_level):
    prompt = f"""
    Generate exactly 4 unique interview questions for the job title: "{job_type}".
    The questions must match the interview level: "{interview_level}".
    
    Interview level meaning:
    - Basic_Level: beginner-friendly, simple concepts, practical examples.
    - Intermediate_level: moderate complexity, mix of theory and practice.
    - Advance_level: deep technical, specialized, challenging scenarios.
    
    Requirements:
    - Avoid repeating question patterns.
    - Ensure each question is clear, specific to the job, and includes at least one scenario-based question.
    - Format strictly as:
    1. Question text
    2. Question text
    3. Question text
    4. Question text
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a job interviewer who generates smart, relevant questions based on the given job type."},
            {"role": "user", "content": prompt}
        ]
    )

    # The raw content from OpenAI
    raw_output = response['choices'][0]['message']['content'].strip()

    # DEBUG: print to check what came back
    # print("RAW OPENAI RESPONSE >>>", raw_output)

    # Convert string into list of questions
    questions = [line.strip() for line in raw_output.split('\n') if line.strip()]
    
    # Optionally, trim the numbers like "1. ", "2. ", etc.
    cleaned_questions = [q.split('. ', 1)[1] if '. ' in q else q for q in questions]

    return cleaned_questions
