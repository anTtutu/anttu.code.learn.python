# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  气泡图
@Author         :  Anttu
@Version        :  v1.0
@File           :  testBubble.py
@CreateTime     :  7/6/2021 15:38
"""

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
fileName = "bubble.csv"
outFileName = "request_bubble.jpg"

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
    value = data.loc[:, ]

    x = value['x']
    y = value['y']
    s = value['size']*200
    colors = value['size']

    # 设置画布
    plt.figure(dpi=100, figsize=(24, 32))
    # 散点图的变种气泡图
    plt.scatter(x, y, s=s, c=colors, label='Size值分布', alpha=0.5)
    # 显示图例
    # plt.legend('Size')
    # X坐标-横坐标标题
    plt.xlabel(u'X坐标刻度', size=24)
    # Y坐标-纵坐标标题
    plt.ylabel(u'Y坐标刻度', size=24)
    # 统计图的标题
    plt.title(u"XX值分布气泡图", size=32)
    # 网格
    plt.grid(True)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
