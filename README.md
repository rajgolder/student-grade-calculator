# Student Grade Calculator

A basic Python program that:

- Takes marks for **5 subjects** (English, Biology, Physics, Chemistry, Math)
- Calculates **total** and **percentage**
- Assigns a **grade** (A, B, C, D, or Fail)
- Prints a formatted report card

---

## Grading Scale

| Percentage | Grade |
|------------|-------|
| 90 – 100   | A     |
| 80 – 89    | B     |
| 70 – 79    | C     |
| 60 – 69    | D     |
| Below 60   | Fail  |

---

## How to Run

1. Save the code as `grade_calculator.py`
2. Open a terminal / command prompt in that folder
3. Run:
   ```bash
   python grade_calculator.py
   ```
4. Enter marks for each subject when prompted

---

## The Code

```python
# Student Grade Calculator - 5 subjects
print("=== Student Grade Calculator ===")

eng = int(input("Enter marks in English: "))
bio = int(input("Enter marks in Biology: "))
phy = int(input("Enter marks in Physics: "))
chem = int(input("Enter marks in Chemistry: "))
math = int(input("Enter marks in Math: "))

total = eng + bio + phy + chem + math
percentage = (total / 500) * 100

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

print("\n" + "="*30)
print("          REPORT CARD")
print("="*30)
print(f"English        : {eng}")
print(f"Biology        : {bio}")
print(f"Physics        : {phy}")
print(f"Chemistry      : {chem}")
print(f"Mathematics    : {math}")
print("-"*30)
print(f"Total Marks    : {total} / 500")
print(f"Percentage     : {percentage:.2f}%")
print(f"Grade          : {grade}")
print("="*30)
```

---

## Example Output

```
=== Student Grade Calculator ===
Enter marks in English: 85
Enter marks in Biology: 78
Enter marks in Physics: 92
Enter marks in Chemistry: 65
Enter marks in Math: 70

==============================
          REPORT CARD
==============================
English        : 85
Biology        : 78
Physics        : 92
Chemistry      : 65
Mathematics    : 70
------------------------------
Total Marks    : 390 / 500
Percentage     : 78.00%
Grade          : C
==============================
```

---

## Requirements

- Python 3.x (no extra libraries needed)

---