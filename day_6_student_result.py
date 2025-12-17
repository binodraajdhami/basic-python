math = 90
english = 80
nepali = 32

total = math + english + nepali
percentage = (total/300) * 100
remark = ""
division = ""

if (math >= 32 and english >= 32 and nepali >= 32):
    remark = True
else:
    remark = False

if (remark):

    # check distinction
    if (percentage >= 80 and percentage <= 100):
        division = "Distiction"

    # Check first
    if (percentage >= 60 and percentage < 80):
        division = "First"

    # check second
    if (percentage >= 50 and percentage < 60):
        division = "Second"

    # check third
    if (percentage >= 32 and percentage < 49):
        division = "Third"

else:
    division = "N/A"

print(f"Total: {total}")
print(f"Percentage: {round(percentage, 2)}%")
print(f"Remark: {'Passed' if remark else 'Failed'}")
print(f"Divisioin: {division}")
