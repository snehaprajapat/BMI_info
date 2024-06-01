weight=float(input("Enter weight in kg : "))
height=float(input("Enter height in m : "))
BMI = round(weight/height ** 2)


if BMI<18.5:
    print(f"Your BMI is {BMI} and you are Under weight.")
elif BMI<25.0:
    print(f"Your BMI is {BMI} and you are Normal weight.")
elif BMI<30:
    print(f"Your BMI is {BMI} and you are over weight.")
elif BMI<35:
    print(f"Your BMI is {BMI} and you are Obese.")
else:
    print(f"Your BMI is {BMI} and you are Clinically Obese.")