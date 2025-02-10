Height = float(input("Enter your Height in meters: "))
weight = float(input("Enter your Weight in kilograms: "))
BMI = weight / (Height * Height)

#perform calculation based on the operator
if BMI < 18.5:
    print('You are underweight.')
elif BMI >= 18.5 and BMI <= 25:
    print('You are normal weight.')
elif BMI >= 25 and BMI <= 30:
    print('You are overweight.')
elif BMI > 30:
    print('You are clinically obese.')



#Take 2
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    classification = 'Underweight'
if bmi < 25:
    classification = 'Normal Weight'
if bmi < 30:
    classification = 'Overweight'
else:
    classification = 'Clinically obese'

print(f'Your BMI is {bmi:.2f}. which is considered {classification}.')
