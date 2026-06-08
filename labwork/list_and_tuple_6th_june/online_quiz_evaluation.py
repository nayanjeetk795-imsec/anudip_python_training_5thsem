correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
correct_count = 0
wrong_count = 0
wrong_questions = []

for i in range(len(correct)):
    if student[i] == correct[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1
        wrong_questions.append(i + 1)  # Question numbers start from 1

percentage = (score / len(correct)) * 100

print("Score:", score, "/", len(correct))
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Incorrectly Answered Questions:", wrong_questions)

print("Percentage:", percentage, "%")

if percentage >= 60:
    print("Pass")
else:
    print("Fail")