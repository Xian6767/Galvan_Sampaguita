# Xyrene P. Galvan
# 8-Sampaguita
def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
    print("=============================")

display_header()

def get_student_info():
name = input("Enter Student Name: ")
# Local Variable 1
assessment1 = float(input("Enter Assessment 1: "))
# Local Variable 2
assessment2 = float(input("Enter Assessment 2: "))
assessment3 = float(input("Enter Assessment 3: "))

get_student_info()

def evaluate_performance():
average = assessment1 +  assessment2 + assessment3 / 3

if average >= 90:
     level = "Outstanding"
elif average >= 85:
    level = "Very Satisfactory"
elif average >= 80:
    level = "Satisfactory"
elif average >= 75:
    level = "Fairly Satisfactory"
else:
    level = "Needs Improvement"

evaluate_performance()

def display_report():
    print(f"{name}")
    print(f"{assessment1}, {assessment2}, {assessment3}")
    print(f"{average}")
    print(f"{level:.2f}")

display_report()
