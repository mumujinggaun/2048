import random

def ran_num(v):
    '''随机在空白位置增加一个数字2或4'''
    if random.random() < 0.9:
        num = 2
    else:
        num = 4

    s =[]
    for i in range(4):
        for j in range(4):
            if v[i][j] == 0:
                s.append((i,j))
                #print(s)
    if len(s) != 0:
        x,y = random.choice(s)
        v[x][y] = num
        return 0
    else:
        return 1 #游戏结束

def display(v):
    '''打印出来4*4的各个数字值'''
    for i in range(4):
        print('{0:6d} {1:6d} {2:6d} {3:6d}'.format(v[i][0],v[i][1],v[i][2],v[i][3]))

def max(v):
    '''屏幕上的最大值'''
    max = 0
    for i in range(4):
        for j in range(4):
            if v[i][j] > max:
                max = v[i][j]
    return max

def direc(x,v,score):

    if x == 8:#上
        a = 0
        b = 1
    elif x == 2:#下
        a = 0
        b = -1
    elif x == 4:#左
        a = 1
        b = 1
    else:# x == 6,右
        a = 1
        b = -1

    for j in range(4):
        num = []
        n = False
        for i in range(4)[::b]:
            if a == 0:
                if v[i][j] != 0: #取出一列中不等于0的数字
                    num.append(v[i][j])
            else: #a==1
                if v[j][i] != 0: #取出一列中不等于0的数字
                    num.append(v[j][i])
        #print(num)
        if len(num) > 1:
            for i in range(len(num)-1):
                if n == False: #相同的数字只合并一次
                    if num[i] == num[i+1]: #如果两个数相等合并
                        score += num[i]
                        num[i] = 2 * num[i]
                        del num[i+1]
                        n = True
                else:
                    break
        #print(num)
        if len(num) < 4: #重新排序，集中到一边
            if a == 0:
                if b == 1:
                    for i in range(len(num)):
                        v[i][j] = num[i]
                    for i in range(len(num),4):
                        v[i][j] = 0
                else: #b==-1
                    for i in range(4-len(num),4)[::-1]:
                        v[i][j] = num[(4-1)-i]
                    for i in range(4-len(num)):
                        v[i][j] = 0
            else: #a == 1
                if b == 1:
                    for i in range(len(num)):
                        v[j][i] = num[i]
                    for i in range(len(num),4):
                        v[j][i] = 0
                else: #b==-1
                    for i in range(4-len(num),4)[::-1]:
                        v[j][i] = num[(4-1)-i]
                    for i in range(4-len(num)):
                        v[j][i] = 0
    return score


v = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
score = 0
#在空白处添加两个数字，并显示出来
ran_num(v)
ran_num(v)
display(v)

while max(v) < 2048:
    drc=input("请输入方向（上8下2左4右6）：")
    score = direc(int(drc),v,score)
    #display(v)
    state = ran_num(v)
    print('得分合计：{0}'.format(score))
    display(v)
    if state == 1:
        print("you lost")
        break
if state == 0:
    print("you win")
