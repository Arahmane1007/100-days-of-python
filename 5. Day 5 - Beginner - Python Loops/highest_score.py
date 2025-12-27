
student_score = input("Input a list of student_score\n").split()

for n in range(0, len(student_score)):
    student_score[n]= float(student_score[n])

highest_score = student_score[0]

for score in student_score:
    if score > highest_score:
        highest_score = score


print(f"The highest score is {highest_score}")


