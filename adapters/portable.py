from tools.create_interview_plan import run as create_interview_plan
from tools.generate_practice_questions import run as generate_practice_questions
from tools.review_interview_answer import run as review_interview_answer

TOOLS = {
    "create-interview-plan": create_interview_plan,
    "generate-practice-questions": generate_practice_questions,
    "review-interview-answer": review_interview_answer,
}

def invoke(name, input_data):
    if name not in TOOLS:
        raise ValueError(f"unknown tool: {name}")
    return TOOLS[name](input_data)
