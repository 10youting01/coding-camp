# BMI 計算器

height = float(input("請輸入你的身高(單位:公尺):"))
weight = float(input("請輸入你的體重(單位:公斤):"))
BMI = weight / (height**2)
print ("你的BMI是:" + str(round(BMI, 2))) # round