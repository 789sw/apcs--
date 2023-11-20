#https://zerojudge.tw/ShowProblem?problemid=a005

t = input()
t_list = []
for i in range(t) :
    for j in range(4):
        t_list[i][j] = input()
for i in range(t):
    for j in range(4):
        print (t_list[i][j],end = " ") 
    print("\n")
#其中end=",意思是为末尾end传递一个空字符串，
# 这样print函数不会在字符串末尾添加一个换行符，
# 而是添加一个空字符串，其实这也是一个语法要求，
# 表示这个语句没结束。
#print默认是打印一行，结尾加换行。end=’ '意思是末尾不换行，加空格。

