print("Welcome to our BMI  calculator!")

height = float(input("Enter your height in cm: "))

weight = float(input("Enter your weight in kg: "))

bmi = weight /(height/100) **2

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You are slightly overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
print(f"Your BMI is {bmi:.2f}")