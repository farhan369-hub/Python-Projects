def validate_answers():
    correct = ["A", "B", "C", "D", "A"]
    answers = []
    for i in range(5):
        a = input("Enter answer: ")
        answers.append(a)
    return answers, correct
def calculate_score(answers, correct):
    score = 0
    for i in range(len(correct)):
        if answers[i] == correct[i]:
            score = score + 1
    return score
def generate_grade(score):
    if score == 5:
        return "A"
    elif score >= 4:
        return "B"
    elif score >= 3:
        return "C"
    elif score >= 2:
        return "D"
    else:
        return "F"

answers, correct = validate_answers()
score = calculate_score(answers, correct)
grade = generate_grade(score)

print("Score:", score)
print("Grade:", grade)