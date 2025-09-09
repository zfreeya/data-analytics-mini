import pandas as pd
import os

user_level = pd.read_excel("D:/新建文件夹/【课程3.0】Python基础与分析实战/【课程3.0】Python基础与分析实战/python第三讲资料/danmu/user_level.xlsx")

excel_list = []
for item in os.listdir(
    "D:\新建文件夹\【课程3.0】Python基础与分析实战\【课程3.0】Python基础与分析实战\python第三讲资料\danmu"):#返回指定路径下有哪些文件
    if 'xlsx' in item and 'user_level' not in item:
        excel_list.append(item)
        print( excel_list)
danmu = pd.DataFrame

