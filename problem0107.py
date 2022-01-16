# BMI 計算器
# BMI 檢測器

height = float(input("Please input your height (in meters):"))
weight = float(input("Please input your weight (in kilograms):"))
BMI = weight / (height**2)
print ("Your BMI is:" + str(round(BMI, 2))) # round

if BMI < 18.5:
    print ("You are underweight")
elif BMI >= 18.5 and BMI <= 24:
    print ("You are just fit.")
else:
    print ("You are overweight")