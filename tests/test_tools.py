from core.analysis import create_interview_plan, generate_practice_questions, review_interview_answer
import pytest

def test_plan():
    r = create_interview_plan("Data Analyst", ["Python"], ["SQL"])
    assert r["role"] == "Data Analyst"
    assert r["focus_areas"][0]["skill"] == "Python"

def test_questions():
    r = generate_practice_questions(["Python"], ["technical"])
    assert len(r["questions"]) == 1
    assert r["questions"][0]["topic"] == "Python"

def test_review():
    r = review_interview_answer("Tell me about Python", "I use Python for data analysis.", ["Python"])
    assert r["criteria_review"]["Python"]["addressed"] is True

def test_invalid_plan():
    with pytest.raises(ValueError):
        create_interview_plan("", ["Python"], ["SQL"])

def test_invalid_answer():
    with pytest.raises(ValueError):
        review_interview_answer("Question", "", ["relevance"])
