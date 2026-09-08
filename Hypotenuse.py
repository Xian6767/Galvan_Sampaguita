import math

lengtha = float(input("Whats the length of side a: "))
lengthb = float(input("Whats the length of side b: "))

hypotenuse = math.sqrt(math.pow(lengtha, 2) + math.pow(lengthb, 2))

print(f"The hypotenuse is {hypotenuse:.2f}")