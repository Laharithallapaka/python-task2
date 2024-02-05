"""Task-2:
        BMI CALCULATOR"""


weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

height_in_meters = height / 100

BMI = weight / (height_in_meters ** 2)

if BMI < 16:
    print("You are surely Underweight")
elif 16 <= BMI < 18.5:
    print("You are Underweight")
elif 18.5 <= BMI < 24:
    print("You are healthy")
elif 25 <= BMI < 30:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")
