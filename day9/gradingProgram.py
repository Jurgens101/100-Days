#calculating student grades using dictionaries

studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Neville": 62
}

studentGrades = {}

for student in studentScores:
    score = studentScores[student]
    if score > 90:
        studentGrades[student] = "Outstanding"
    elif score > 80: 
        studentGrades[student] = "Exceeds Expectations"
    elif score >70:
        studentGrades[student] = "Acceptable"
    else:
        studentGrades[student] = "Fail"

print(studentGrades)

