import re

student_Id = input("Enter Student ID: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_Id):
    print("Valid Student ID")

else:
    print("Invalid Student ID")