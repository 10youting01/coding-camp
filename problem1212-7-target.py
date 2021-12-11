# coding camp hand in 12/12 12:00
# problem num 7
# 請寫一隻程式，輸入一串數字並且用逗號隔開，如：「2,3,4,5,6」 
# 接著輸入目標總數，如：「9」，請輸出一開始輸入的那串數字中
# 哪兩個數字加起來會剛好是目標總數，如：「3,6 4,5」
# 輸入輸出除有要求用逗號之外，其餘用換行或空格隔開皆可。

num = input('請輸入數字，以逗號的格式隔開數字 : ')
b = num.split(',')
length = len(b)

target = int(input('請輸入目標數字 : '))
for i in range(length):
    b[i] = int(b[i])
for i in range(0, length, 1):
    for j in range(i+1, length, 1):
        # print(b[i], b[j])
        if (b[i] + b[j]) == target:
            print(b[i], '+', b[j])

