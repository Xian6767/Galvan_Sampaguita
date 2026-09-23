grade = int(input("What is your grade?(0-100): "))

if 0 <= grade <= 100:
    print("Valid grade")

else:
    print("Invalid grade. Grade must be between 0 and 100")