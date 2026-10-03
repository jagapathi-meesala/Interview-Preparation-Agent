from core.analysis import review_interview_answer
def run(input_data):
    return review_interview_answer(input_data["question"], input_data["answer"], input_data["criteria"])
