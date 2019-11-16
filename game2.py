# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 06:37:48 2018

@author: xcl
"""

#!/usr/bin/python3
#coding:utf-8
from tkinter import *
from random import randint
import os

GAME_SIZE=4
BACKGROUND_COLOR = "#94877a"
EMPTY_COLOR = "#afa79a"
#不同数字的背景颜色
GRID_COLOR = {2:"#efe5dd", 4:"#eee2c9", 8:"#f4b37a", 16:"#f79466", 32:"#f87d60", 64:"#f85f3d", 128:"#efcf73", 256:"#eecd63", 512:"#eecA52", 1024:"#efc740", 2048:"#efc42f" }
#不同数字的颜色
FONT_COLOR = { 2:"#7a6f67", 4:"#7a6f69", 8:"#faf9f4", 16:"#faf6f2", 32:"#faf8f6", 64:"#fbfaf5", 128:"#fbfaf8", 256:"#faf8f8", 512:"#faf8f8", 1024:"#faf8f8", 2048:"#faf8f8" }

#生成空的矩阵
def getEmptyMatrix():
    mat=[]
    for i in range(GAME_SIZE):
        mat.append([])
        for j in range(GAME_SIZE):
            mat[i].append(0)
    return mat

def operateLeft(mat,grade):
    newGrade=grade
    newMatrix=getEmptyMatrix()
    #矩阵中的数字向左移动合并的操作是否有效，即移动合并好矩阵有没有改变
    done=False
    #将矩阵中的数字从右边移动到左边
    for i in range(GAME_SIZE):
        count=0
        for j in range(GAME_SIZE):
            if mat[i][j]!=0:
                newMatrix[i][count]=mat[i][j]
                count+=1
    #向左合并将矩阵中相邻的数值相同且不为零的数字
    for i in range(GAME_SIZE):
         for j in range(GAME_SIZE-1):
             if newMatrix[i][j]==newMatrix[i][j+1] and newMatrix[i][j]!=0:
                 newMatrix[i][j]*=2
                 newGrade+=newMatrix[i][j]
                 newMatrix[i][j+1]=0
    #将右边的都移动到左边
    newMatrix2=getEmptyMatrix()
    for i in range(GAME_SIZE):
        count=0
        for j in range(GAME_SIZE):
            if newMatrix[i][j]!=0:
                newMatrix2[i][count]=newMatrix[i][j]
                count+=1
    #若进行向左移动合并操作后矩阵发生变化，这该操作有效
    if not (mat==newMatrix):
        done=True
    return (newMatrix2,done,newGrade)

def operateRight(mat,grade):
    newGrade=grade
    newMatrix=getEmptyMatrix()
    #矩阵中的数字向右移动合并的操作是否有效，即移动合并好矩阵有没有改变
    done=False
    #将矩阵中的数字从左边移动到右边
    for i in range(GAME_SIZE):
        count=GAME_SIZE-1
        for j in range(GAME_SIZE):
            j=GAME_SIZE-j-1
            if mat[i][j]!=0:
                newMatrix[i][count]=mat[i][j]
                count-=1
    #向右合并将矩阵中相邻的数值相同且不为零的数字
    for i in range(GAME_SIZE):
         for j in range(GAME_SIZE-1):
             j=GAME_SIZE-j-1
             if newMatrix[i][j]==newMatrix[i][j-1] and newMatrix[i][j]!=0:
                 newMatrix[i][j]*=2
                 newGrade+=newMatrix[i][j]
                 newMatrix[i][j-1]=0
    #将合并后矩阵中的数字从左边移动到右边
    newMatrix2=getEmptyMatrix()
    for i in range(GAME_SIZE):
        count=GAME_SIZE-1
        for j in range(GAME_SIZE):
            j=GAME_SIZE-j-1
            if newMatrix[i][j]!=0:
                newMatrix2[i][count]=newMatrix[i][j]
                count-=1
    #若进行向右移动合并操作后矩阵发生变化，这该操作有效
    if not (mat==newMatrix):
        done=True
    return (newMatrix2,done,newGrade)

def operateUp(mat,grade):
    newGrade=grade
    newMatrix=getEmptyMatrix()
    #矩阵中的数字向上移动合并的操作是否有效，即移动合并好矩阵有没有改变
    done=False
    #将矩阵中的数字从下边移动到上边
    for i in range(GAME_SIZE):
        count=0
        for j in range(GAME_SIZE):
            if mat[j][i]!=0:
                newMatrix[count][i]=mat[j][i]
                count+=1
    #向上合并将矩阵中相邻的数值相同且不为零的数字
    for i in range(GAME_SIZE):
         for j in range(GAME_SIZE-1):
             if newMatrix[j][i]==newMatrix[j+1][i] and newMatrix[j][i]!=0:
                 newMatrix[j][i]*=2
                 newGrade+=newMatrix[j][i]
                 newMatrix[j+1][i]=0
    #将合并后矩阵中的数字从下边移动到上边
    newMatrix2=getEmptyMatrix()
    for i in range(GAME_SIZE):
        count=0
        for j in range(GAME_SIZE):
            if newMatrix[j][i]!=0:
                newMatrix2[count][i]=newMatrix[j][i]
                count+=1
    #若进行向上移动合并操作后矩阵发生变化，这该操作有效
    if not (mat==newMatrix):
        done=True
    return (newMatrix2,done,newGrade)


def operateDown(mat,grade):
    newGrade=grade
    newMatrix=getEmptyMatrix()
    #矩阵中的数字向下移动合并的操作是否有效，即移动合并好矩阵有没有改变
    done=False
    #将矩阵中的数字从上边移动到下边
    for i in range(GAME_SIZE):
        count=GAME_SIZE-1
        for j in range(GAME_SIZE):
            j=GAME_SIZE-j-1
            if mat[j][i]!=0:
                newMatrix[count][i]=mat[j][i]
                count-=1
    #向下合并将矩阵中相邻的数值相同且不为零的数字
    for i in range(GAME_SIZE):
         for j in range(GAME_SIZE-1):
             j=GAME_SIZE-j-1
             if newMatrix[j][i]==newMatrix[j-1][i] and newMatrix[j][i]!=0:
                 newMatrix[j][i]*=2
                 newGrade+=newMatrix[j][i]
                 newMatrix[j-1][i]=0
     #将合并后矩阵中的数字从上边移动到下边
    newMatrix2=getEmptyMatrix()
    for i in range(GAME_SIZE):
        count=GAME_SIZE-1
        for j in range(GAME_SIZE):
            j=GAME_SIZE-j-1
            if newMatrix[j][i]!=0:
                newMatrix2[count][i]=newMatrix[j][i]
                count-=1
    #若进行向下移动合并操作后矩阵发生变化，这该操作有效
    if not (mat==newMatrix):
        done=True
    return (newMatrix2,done,newGrade)

class Game2048(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('2048小游戏')
        self.bind("<Key>", self.getKey)#接收键入
        self.operations = { "'w'": operateUp, "'s'": operateDown, "'a'": operateLeft, "'d'": operateRight }
        self.initWindow()
        self.initMatrix()
        self.mainloop()
    #初始化界面窗口的布局
    def initWindow(self):
        bar=Frame(self)
        bar.grid()
        #初始化界面窗口的积分，记录和重新开始按钮
        self.t = Label(bar, justify=LEFT, font=("Verdana", 25, "bold"))
        self.t.pack(side='left')
        Button(bar, text="重新\n开始", command=self.initMatrix,width=7,font=("Verdana", 20, "bold"),bg=BACKGROUND_COLOR).pack(side='right')
        background = Frame(self, bg=BACKGROUND_COLOR)
        background.grid()
        self.gameGrid = []
        #初始化界面窗口中游戏的格子
        for i in range(GAME_SIZE):
            x = []
            for j in range(GAME_SIZE):
                t = Label(background, justify=CENTER, font=("Verdana", 40, "bold"), width=4, height=2)
                t.grid(row=i, column=j, padx=5, pady=5)
                x.append(t)
            self.gameGrid.append(x)

    #初始化界面，在矩阵中两个随机的地方生成2，并更新显示
    def initMatrix(self):
        self.matrix = getEmptyMatrix()
        self.grade=0
        self.record=0
        self.getNewNumber()
        self.getNewNumber()
        if os.path.exists('record.txt'):
            with open('record.txt', 'r') as f:     # 打开record.txt   如果文件不存在，创建该文件。
                self.record=f.read()  # 把变量var写入test.txt。这里var必须是str格式，如果不是，则可以转一下。
                self.record=int(self.record)
        self.updateShow()
    #更新当前界面的显示
    def updateShow(self):
        #更新分数
        self.t.configure(text="积分:%-15d\n记录:%-15d"%(self.grade,self.record))
        #更新矩阵
        for i in range(GAME_SIZE):
            for j in range(GAME_SIZE):
                x = self.matrix[i][j]
                if x == 0:
                    self.gameGrid[i][j].configure(text="", bg=EMPTY_COLOR)
                else:
                    self.gameGrid[i][j].configure(text=str(int(x)), bg=GRID_COLOR[x], fg=FONT_COLOR[x])
        self.update_idletasks()
    #获取当前的状态 胜利1，继续0，失败-1
    def getState(self):
        #矩阵中出现2048，胜利
        for x in self.matrix:
            if 2048 in x:
                return 1
        #矩阵中有空位，游戏继续
        for x in self.matrix:
            if 0 in x:
                return 0
        #矩阵已满但可以进行合并，即左右或者上下有相邻的数值相同的数字，游戏继续
        for i in range(GAME_SIZE):
            for j in range(GAME_SIZE-1):
                if self.matrix[i][j]==self.matrix[i][j+1] or self.matrix[j][i]==self.matrix[j+1][i]:
                    return 0
        #否则游戏失败
        return -1
    #接受键盘的输入
    def getKey(self, event):
        key = repr(event.char)
        #如果按键在wasd中
        if key in self.operations:
            #执行对应的操作函数
            self.matrix,done,self.grade = self.operations[key](self.matrix,self.grade)
            #按键操作是否执行有效
            if done:
                if self.grade>self.record:
                    with open('record.txt', 'w') as f:     # 打开record.txt   如果文件不存在，创建该文件。
                        f.write(str(int(self.grade)))  # 把变量写入txt
                        self.record=self.grade
                self.getNewNumber()
                self.updateShow()
                nowState=self.getState()
                if nowState==1:
                    #给出游戏胜利的提示
                    self.gameGrid[int(GAME_SIZE/2-1)][int(GAME_SIZE/2-1)].configure(text="胜",bg=EMPTY_COLOR,fg=FONT_COLOR[16])
                    self.gameGrid[int(GAME_SIZE/2-1)][int(GAME_SIZE/2)].configure(text="利!",bg=EMPTY_COLOR,fg=FONT_COLOR[16])
                if nowState==-1:
                    #给出游戏失败的提示
                    self.gameGrid[int(GAME_SIZE/2-1)][int(GAME_SIZE/2-1)].configure(text="失",bg=EMPTY_COLOR,fg=FONT_COLOR[16])
                    self.gameGrid[int(GAME_SIZE/2-1)][int(GAME_SIZE/2)].configure(text="败!",bg=EMPTY_COLOR,fg=FONT_COLOR[16])
    #在矩阵中产生新的2或者4
    def getNewNumber(self):
        index_x=randint(0, GAME_SIZE - 1)
        index_y=randint(0, GAME_SIZE - 1)
        #随机找到为0的坐标
        while self.matrix[index_x][index_y] != 0:
            index_x=randint(0, GAME_SIZE - 1)
            index_y=randint(0, GAME_SIZE - 1)
        if self.grade>2048:#游戏当前的分数大于一定的值产生2或者4
            self.matrix[index_x][index_y] = randint(1, 2)*2
        else:
            self.matrix[index_x][index_y] = 2

def startGame():
    root.destroy()
    gamegrid = Game2048()

if __name__=='__main__':
    root = Tk()             #初始化Tk()
    root.title("游戏简介")
    root.geometry('500x380')
    Label(root, text="游戏简介", bg=BACKGROUND_COLOR, justify=CENTER, font=("Verdana", 40, "bold"), width=6, height=1).pack()
    rule="    2048游戏共有16个格子，初始时\n会有两个格子上安放了两个数字2或4，\n每次可以选择上下左右其中一个方向去\n滑动，每滑动一次，所有的数字方块都\n会往滑动的方向靠拢外，系统也会在空\n白的地方随即出现一个数字方块，相同\n数字的方块在靠拢、相撞时会相加。系\n统给予的数字方块不是2就是4，玩家要\n想法在这小小的16格范围中凑出2048\n这个数字方块。(w:上,s:下,a:左,d:右)"
    Label(root, text=rule, justify=CENTER, font=("Verdana", 16, "bold")).pack()
    Button(root, text="确定", command=startGame,bg=BACKGROUND_COLOR,width=20).pack()
    root.mainloop() #进入消息循环
