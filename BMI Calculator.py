BMI Calculator using if else statement

name = "Atom"
height_m = 2
weight_kg = 110
bmi = weight_kg / (height_m ** height_m)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
