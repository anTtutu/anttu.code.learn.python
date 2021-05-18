# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  
@Author         :  Anttu
@Version        :  v1.0
@File           :  testScatter.py
@CreateTime     :  15/5/2021 21:28
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
fileName = "scatter.csv"
outFileName = "request_scatter.jpg"

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
    total_data = data.loc[:, ]

    height = total_data['身高']
    weight = total_data['体重']

    # 设置画布
    plt.figure(dpi=100, figsize=(24, 32))
    # 散点图
    plt.scatter(height, weight)
    # 显示图例
    plt.legend(('身高/Height', '体重/Weight'))
    # X坐标-横坐标标题
    plt.xlabel(u'身高/Height(厘米)', size=24)
    # Y坐标-纵坐标标题
    plt.ylabel(u'体重/Weight(公斤)', size=24)
    # 统计图的标题
    plt.title(u"XX公司男女身高/体重分布", size=32)
    # 网格
    plt.grid(True)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
