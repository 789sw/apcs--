#https://zerojudge.tw/ShowProblem?problemid=a005

t = int(input())
t_list = []
for i in range(t) : 
    t_list.append([])
    input_line = input().split()  #輸入
    for j in range(4):
        t_list[i].append(int(input_line[j]))  # 將每個部分轉換為整數
    d = t_list[i][1]-t_list[i][0]
    if (t_list[i][0] + d) == t_list[i][1] and (t_list[i][1] + d) == t_list[i][2]:   #判斷是否為公差
        t_list[i][4].append(t_list[i][3] + d)
    else:
        r = t_list[i][1] / t_list[i][0]     #為公比
        t_list[i][4].append(t_list[i][3] * r)

for i in range(t):      #印出結果
    for j in range(5):
        print (t_list[i][j],end = " ") 
    print("\n")
#其中end=" ",意思是为末尾end传递一个空字符串，
# 这样print函数不会在字符串末尾添加一个换行符，
# 而是添加一个空字符串，其实这也是一个语法要求，
# 表示这个语句没结束。
#print默认是打印一行，结尾加换行。end=’ '意思是末尾不换行，加空格。

