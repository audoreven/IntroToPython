

score = float(input("Enter a score: "))

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score < 0.6:
    grade = 'F'

if score > 1.0:
    print("Bad score")
else:
    print("Grade:", grade)