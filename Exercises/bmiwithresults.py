weight = float(input("Enter weight in pounds: "))*0.45359

height = float(input("Enter height in inches: "))*0.0254

bmi = (weight/(height**2))

print("Your BMI is", bmi)

if bmi >= 30:
    print("Obese")
elif 25 <= bmi:
    print("Overweight")
elif 18.5 <= bmi:
    print("Normal")
else:
    print("Underweight")
