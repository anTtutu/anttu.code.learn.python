# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  雷达图
@Author         :  Anttu
@Version        :  v1.0
@File           :  testRadar.py
@CreateTime     :  8/6/2021 10:00
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
fileName = "ninjas.csv"
outFileName = "request_radar_ninja_"

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
    ability_name = data.loc[:, '忍':'印']
    # 名称列
    ability_value = data.loc[:, ]

    # 能力值的名称，需要去掉姓名和合计才可以放到雷达图中
    col_names = data.keys()
    labels = col_names.drop(['姓名', '合计'])
    data_length = len(labels)

    # labels里有几个数据，就把整圆360°分成几份，设置雷达图的角度，用于平分切开一个平面
    angle = np.linspace(0, 2 * np.pi, data_length, endpoint=False)

    # 使雷达图封闭起来
    labels = np.concatenate((labels, [labels[0]]))
    angles = np.concatenate((angle, [angle[0]]))

    for index in range(len(ability_name)):
        # 技能值
        result = ability_name.iloc[index].values

        # 使雷达图封闭起来
        values = np.concatenate((result, [result[0]]))

        # 设置画布
        fig = plt.figure(dpi=100, figsize=(8, 6))

        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        # 绘制折线图
        ax.plot(angles, values, 'o-', linewidth=1)
        ax.fill(angles, values, 'r', alpha=0.5)

        # 添加每个特质的标签
        ax.set_thetagrids(angles * 180 / np.pi, labels)
        # 设置极轴范围
        ax.set_rlim(0, 10)
        # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
        ax.set_rlabel_position(360)
        # 统计图的标题
        title_name = ability_value['姓名'][index]
        plt.title(title_name, size=14)
        # 网格
        plt.grid(True)
        # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
        plt.savefig(os.sep.join([project_dir, outFileName + title_name + '.jpg']))
        # 显示图像
        plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()