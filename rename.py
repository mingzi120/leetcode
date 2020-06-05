
import os
import re
import sys
def renameall():
    fileList = os.listdir(r"G:\儿歌")		#待修改文件夹
    print("修改前："+str(fileList))		#输出文件夹中包含的文件
    currentpath = os.getcwd()		#得到进程当前工作目录
    os.chdir(r"G:\儿歌")		#将当前工作目录修改为待修改文件夹的位置
    num=1		#名称变量
    newfilename=''
    for fileName in fileList:
        newfilename=fileName.replace("[www.susu09.com]","")
        os.rename(fileName,newfilename)
    print("---------------------------------------------------")
    os.chdir(currentpath)		#改回程序运行前的工作目录
    sys.stdin.flush()		#刷新
    # print("修改后："+str(os.listdir(r"W:\儿童\凯叔讲故事-凯叔西游记1-5部全137集mp3\凯叔西游记第三部")))		#输出修改后文件夹中包含的文件

renameall()
