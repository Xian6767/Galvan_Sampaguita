#Global Variable 1
n1 = float(input("Please enter the first number: "))
#Global Variable 2
n2 = float(input("Please enter the second number: "))

def calculate_sum():
    #Local Variable 1
    sum = n1 + n2
    print("The sum is", sum)

def calculate_difference():
    #Local Variable 2
    difference = n1 - n2
    print("The difference is", difference)

calculate_sum()
calculate_difference()