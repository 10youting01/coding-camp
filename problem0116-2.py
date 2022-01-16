# 樹狀星星
# 雙重迴圈練習

n = int(input("Please enter a number:"))

for i in range(1,n+1,1):
    for j in range(1,2*n,1):
        if j == n-i+1:
            for k in range(2*i-1):
                print ("*",end='')
        else:
            print (" ",end='')
    print ("\n")
