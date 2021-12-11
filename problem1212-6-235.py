# coding camp hand in 12/12 12:00
# problem num 6
# 讓使用者能輸入數字，而電腦必須輸出此數字是2的倍數還是3的倍數還是5的倍數
# 若輸入的數值為一種數字以上的倍數(例如:15是5及3的倍數)，請都需要輸出，若無請回復無。

print('Please input a number:')
inNum = int(input())
if inNum % 2 == 0:
    print(inNum,'是2的倍數')
if inNum % 3 == 0:
    print(inNum,'是3的倍數')
if inNum % 5 == 0:
    print(inNum,'是5的倍數')
else:
    print(inNum,'並非2、3、5的倍數')
