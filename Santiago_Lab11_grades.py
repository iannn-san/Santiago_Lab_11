grades = []
passingcount = 0

for i in range(5):
    grade = float(input(f"Enter grade for student {i+1}, input grades between 40-100: "))
    if 40 <= grade <= 100:
        grades.append(grade)
        if grade >= 75:
            passingcount += 1
    else:
        print("Grade must be between 40 and 100.")
        break
# my calculator para sa  average grade
avgrade = sum(grades) / len(grades)

# my calculator para passing percentage ng students
passpercentage = (passingcount / len(grades)) * 100

print("\ngrades inputted:", grades)
print("average grade is:", round(avgrade, 2))
print("number of students with the passing grade is:", passingcount)
print("passing percentage is:", round(passpercentage, 2), "%")