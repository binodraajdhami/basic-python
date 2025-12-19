# SLC Result, min_pass_mark = 35
# Function


min_pass_mark = 32

student_name = "Ram"
math = 90
english = 90
nepali = 90
social = 90
computer = 31

total = math + english + nepali + social + computer
percentage = round((total/500) * 100, 2)
remark = False
division = "N/A"

if (
        math >= min_pass_mark and
        english >= min_pass_mark and
        nepali >= min_pass_mark and
        social >= min_pass_mark and
        computer >= min_pass_mark):
    remark = True
else:
    remark = False

if (remark):
    if (percentage >= 80 and percentage <= 100):
        division = "Distinction"

    elif (percentage >= 60 and percentage < 80):
        division = "First"

    elif (percentage >= 50 and percentage < 60):
        division = "Second"

    elif (percentage >= 32 and percentage < 50):
        division = "Third"
else:
    division = "N/A"

print(f"Total : {total}")
print(f"Percentage : {percentage}%")
print(f"Remark : {"Passed" if (remark) else "Failed"} ")
print(f"Division: {division}")
