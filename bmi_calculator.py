#!/usr/bin/env python

height = input("Please enter your height in metres (m): ")
weight = input("Please enter your weight in kilograms (kg): ")

bmi = round(float(weight) / (float(height) ** 2))

if bmi >= 35:
    print(f"Your bmi is {bmi}, and you are clinically obese.")
elif bmi >= 30:
    print(f"Your bmi is {bmi}, and you are obese.")
elif bmi >= 25:
    print(f"Your bmi is {bmi}, and you are overweight.")
elif bmi >= 18.5:
    print(f"You bmi is {bmi}, and you are normal weight.")
else:
    print(f"Your bmi is {bmi}, and you are underweight.")