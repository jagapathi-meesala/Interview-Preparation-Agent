def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()

def _strings(values, name):
    if not isinstance(values, list) or not values:
        raise ValueError(f"{name} must be a non-empty list")
    out = []
    for v in values:
        out.append(_text(v, name))
    return out

def create_interview_plan(role, skills, topics):
    role = _text(role, "role")
    skills = _strings(skills, "skills")
    topics = _strings(topics, "topics")
    return {"role": role, "focus_areas": [{"skill": s, "topics": topics} for s in skills]}

def generate_practice_questions(topics, question_types):
    topics = _strings(topics, "topics")
    question_types = _strings(question_types, "question_types")
    questions = []
    for topic in topics:
        for qtype in question_types:
            questions.append({"topic": topic, "type": qtype, "question": f"Explain your experience with {topic} and provide a concrete example."})
    return {"questions": questions}

def review_interview_answer(question, answer, criteria):
    question = _text(question, "question")
    answer = _text(answer, "answer")
    criteria = _strings(criteria, "criteria")
    observations = {}
    lower = answer.lower()
    for criterion in criteria:
        key = criterion.strip()
        observations[key] = {
            "addressed": key.lower() in lower,
            "evidence": "criterion term appears in the supplied answer" if key.lower() in lower else "criterion term was not explicitly found in the supplied answer"
        }
    return {"question": question, "criteria_review": observations}
