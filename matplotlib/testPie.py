# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import platform

# 系统
print(platform.system())

# 相对路径
project_dir = os.path.abspath('.')
print(project_dir)
fileName = "pie.csv"
outFileName = "request_pie.jpg"

fontName = "SimHei"
if platform.system() == 'Windows':
    print('Windows系统')
    fontName = ["SimHei"]
elif platform.system() == 'Linux':
    print('Linux系统')
    fontName = ["SimHei"]
elif platform.system() == 'Darwin':
    print('MacOS系统')
    fontName = ["PingFang HK"]
else:
    print('其他')

# Mac字体 PingFang HK
# win字体 SimHei
plt.rcParams['font.sans-serif'] = fontName
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


filePath = os.sep.join([project_dir, fileName])
outPath = os.sep.join([project_dir, outFileName])

# 全路径
# filePath = "D:\\request.csv"
# outPath = "D:\\request.jpg"


def main():
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(filePath, encoding='utf-8')
    # 读取列名
    label_list = data.loc[:, '月份']
    money_list = data.loc[:, '销售']

    # 取最大的份额突出展示，先获取最大份额的索引
    money_max_index = money_list[money_list == money_list.max()].index

    # 设定各项距离圆心n个半径
    explode = []
    for i in range(len(label_list)):
        if i == money_max_index:
            explode.append(0.1)
        else:
            explode.append(0.0)

    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 饼状图
    plt.pie(money_list, explode=explode, labels=label_list, autopct='%1.1f%%', textprops={'fontsize': 43, 'color': 'k'}, shadow=None, startangle=90)
    # 设置为正圆
    plt.axis('equal')
    # 显示图例
    plt.legend()
    # 统计图的标题
    plt.title(u"XX公司部门每月销售额", size=32)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
