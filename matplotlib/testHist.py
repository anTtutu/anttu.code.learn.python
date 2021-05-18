# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  
@Author         :  Anttu
@Version        :  v1.0
@File           :  testHist.py
@CreateTime     :  1/5/2021 11:24
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
fileName = "hist.csv"
outFileName = "request_hist.jpg"

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
    # 读取列名为距离误差和时间点的所有行数据
    round1_list = data.loc[:, '科目1成绩']
    round2_list = data.loc[:, '科目2成绩']
    round3_list = data.loc[:, '科目3成绩']
    round4_list = data.loc[:, '科目4成绩']
    # round_list = data.loc[[1, 2, 3, 4]]
    c = ['r', 'b', 'g', 'y']

    # 设置画布
    plt.figure(dpi=100, figsize=(24, 32))
    # 直方图
    plt.hist([round1_list, round2_list, round3_list, round4_list], histtype='bar', color=c, rwidth=0.8)
    # 显示图例
    plt.legend(('科目1', '科目2', '科目3', '科目4'))
    # X坐标-横坐标标题
    plt.xlabel(u'科目成绩/区间', size=24)
    # Y坐标-纵坐标标题
    plt.ylabel(u'科目成绩/频率', size=24)
    # 统计图的标题
    plt.title(u"XX驾校成绩", size=32)
    # 网格
    plt.grid(True)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
