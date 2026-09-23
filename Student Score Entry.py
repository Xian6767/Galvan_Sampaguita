try:
    score = int(input("Enter Examination Score(0-100): "))

    if 0 <= score <= 100:
        print("Valid Score")

    else:
        print("Invalid Score. Please enter a number between 0 and 100")
except ValueError:
    print("Invalid input. Please enter a number")