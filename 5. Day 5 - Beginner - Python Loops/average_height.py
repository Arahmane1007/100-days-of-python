
student_heights = input("Input a list of student's heights \n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_height = 0
count = 0
for height in student_heights:
    total_height += height
    count += 1

average_height = round(total_height / count)
print(f"Average height: {average_height}")