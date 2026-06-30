# Display the title of the program
print("==== Student Grade Calculator ====")

# Input marks for each subject from the user
eng = int(input("Enter your marks in English: "))
bio = int(input("Enter your marks in Biology: "))
phy = int(input("Enter your marks in Physics: "))
chem = int(input("Enter your marks in Chemistry: "))
math = int(input("Enter your marks in Mathematics: "))

# Calculate total marks and percentage obtained
total = eng + bio + phy + chem + math
percentage = (total / 500) * 100

# Assign a grade based on the percentage range
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

# Print the report card header and subject-wise marks
print("="*30)
print("          REPORT CARD")
print("="*30)
print(f"English        : {eng}")
print(f"Biology        : {bio}")
print(f"Physics        : {phy}")
print(f"Chemistry      : {chem}")
print(f"Mathematics    : {math}")
print("-"*30)

# Display total marks, percentage, and final grade
print(f"Total Marks    : {total} / 500")
print(f"Percentage     : {percentage:.2f}%")
print(f"Grade          : {grade}")
print("="*30)