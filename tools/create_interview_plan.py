from core.analysis import create_interview_plan
def run(input_data):
    return create_interview_plan(input_data["role"], input_data["skills"], input_data["topics"])
