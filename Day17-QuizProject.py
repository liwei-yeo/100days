from Day17_2_question_model import Question
from Day17_1_data import question_data
from Day17_3_quiz_brain import QuizBrain


question_bank = []
for item in question_data["results"]:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {brain.score}/{brain.question_number}.")

