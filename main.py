import pygame, sys



# 设置参数
screen_height = 700
screen_width = 700
checkerboard_background = [238, 121, 66] #设置棋盘背景
line_color = [0,0,0] #设置线条颜色，[0,0,0]对应黑色
checkerboard_pos = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], ]
STEP = 1

'''def clear_pos(checkerboard_pos):
    for i in range(15):
        for j in range(15):
            checkerboard_pos[i][j] = 0'''


def check_over_pos(x, y, checkerboard_pos):
    if checkerboard_pos[x][y] == 0:
        return True
    return False
flag=False
tim=0

def find_pos1(x,y):
    #找到显示的可以落子的位置
    for i in range(15):
        for j in range(15):
            L1=10+40*i-20
            L2=10+40*i+20
            R1=10+40*j-20
            R2=10+40*j+20
            if x>=L1 and x<=L2 and y>=R1 and y<=R2:
                return i, j
    return x,y


def find_pos2(x,y):
    #找到显示的可以落子的位置
    for i in range(10,570,40):
        for j in range(10,570,40):
            L1=i-22
            L2=i+22
            R1=j-22
            R2=j+22
            if x>=L1 and x<=L2 and y>=R1 and y<=R2:
                return i,j
    return x,y


def check_win(x, y ,checkerboard_pos, thrth):
    score = 1
    # 上下方向
    for i in range(1,5):
        if checkerboard_pos[x][y+i] != thrth:
            break
        score += 1


    for i in range(1,5):
        if checkerboard_pos[x][y-i] != thrth:
            break
        score += 1

    if score == 5:
        return thrth

    score = 1
    # 左右方向
    for i in range(1,5):
        if checkerboard_pos[x+i][y] != thrth:
            break
        score += 1

    for i in range(1,5):
        if checkerboard_pos[x-i][y] != thrth:
            break
        score += 1

    if score == 5:
        return thrth
    
    score = 1
    # 左斜
    for i in range(1,5):
        if checkerboard_pos[x-i][y-i] != thrth:
            break
        score += 1

    for i in range(1,5):
        if checkerboard_pos[x+i][y+i] != thrth:
            break
        score += 1
    
    if score == 5:
        return thrth

    score = 1
    # 右斜
    for i in range(1,5):
        if checkerboard_pos[x+i][y-i] != thrth:
            break
        score += 1

    for i in range(1,5):
        if checkerboard_pos[x-i][y+i] != thrth:
            break
        score += 1
    
    if score == 5:
        return thrth
    return 0


# 对屏幕进行初始设置
pygame.init()
screen = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption("五子棋")

# 开始游戏设置
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #画棋盘
    screen.fill(checkerboard_background)
    pygame.draw.line(screen, line_color, [10, 10], [10, 570], 4)
    pygame.draw.line(screen, line_color, [570, 10], [570, 570], 4)
    pygame.draw.line(screen, line_color, [10, 10], [570, 10], 4)
    pygame.draw.line(screen, line_color, [10, 570], [570, 570], 4)
    for i in range(50, 570, 40):
       pygame.draw.line(screen, line_color, [i,10], [i,570], 2)
    for i in range(50, 570, 40):
        pygame.draw.line(screen, line_color, [10, i], [570, i], 2)
    pygame.draw.circle(screen, [0, 0, 0], [290, 290], 5, width=0)

    #获取鼠标坐标信息
    x,y = pygame.mouse.get_pos()

    x,y=find_pos1(x,y)
    pygame.draw.rect(screen,[0 ,229 ,238 ],[10+40*x-20,10+40*y-20,40,40],2,1)

    keys_pressed = pygame.mouse.get_pressed()#获取鼠标按键信息
    #鼠标左键表示落子,tim用来延时的，因为每次循环时间间隔很断，容易导致明明只按了一次左键，却被多次获取，认为我按了多次
    if keys_pressed[0] and tim==0:
        flag=True
        if check_over_pos(x,y,checkerboard_pos):#判断是否可以落子，再落子
            if STEP%2==0:#黑子
                checkerboard_pos[x][y] = 1
                STEP += 1
                if check_win(x, y, checkerboard_pos, 1) == 1:
                    print('black win') 
                    pygame.display.update()#刷新显示

            else:
                checkerboard_pos[x][y] = 2
                STEP += 1
                if check_win(x, y, checkerboard_pos, 2) == 2:
                    print('white win')
                    pygame.display.update()#刷新显示


    #鼠标左键延时作用
    if flag:
        tim+=1
    if tim%200==0 and tim != 0:#延时200ms
        flag=False
        tim=0
        '''for i in checkerboard_pos:
            print(i)
        print('\n')'''

    for i in range(15):#显示所有落下的棋子
        for j in range(15):
            val = checkerboard_pos[i][j]
            if val == 1:
                pygame.draw.circle(screen, [0, 0, 0],[10+40*i,10+40*j], 20,0)
            if val == 2:
                pygame.draw.circle(screen, [255, 255, 255],[10+40*i,10+40*j], 20,0)
    pygame.display.update()