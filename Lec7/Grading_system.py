students_scores = {
"Harry":81,
"Ron":78,
"Alex":99,
"Jack":62,
}

student_grades = {}

for student in students_scores:
    score = students_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)