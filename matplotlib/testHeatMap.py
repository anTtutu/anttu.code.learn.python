# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  热力图
@Author         :  Anttu
@Version        :  v1.0
@File           :  testHeatMap.py
@CreateTime     :  19/5/2021 01:39
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
fileName = "heatmap.csv"
outFileName = "request_heatmap.jpg"

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
    data_nba = pd.read_csv(filePath, encoding='utf-8')
    # 读取列名
    score = data_nba.loc[:, "G":"PF"].values
    # 名称列
    name = data_nba.iloc[:, 0]
    # 技术指标行
    col = data_nba.loc[:, "G":"PF"].columns

    # 设置画布
    fig = plt.figure(dpi=100, figsize=(24, 32))
    # 散点图的变种气泡图
    im = plt.imshow(score, cmap='plasma_r')
    # 设置X轴刻度
    plt.xticks(np.arange(len(col)), col.values)
    # 设置Y轴刻度
    plt.yticks(np.arange(len(name)), name.values)
    # 显示图例
    # plt.legend()
    # 设置颜色条
    fig.colorbar(im, pad=0.03)
    # X坐标-横坐标标题
    plt.xlabel(u'技术指标', size=24)
    # Y坐标-纵坐标标题
    plt.ylabel(u'姓名', size=24)
    # 统计图的标题
    plt.title(u"NBA Average Performance (Top 50 Players)", size=32)
    # 网格
    plt.grid(True)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()