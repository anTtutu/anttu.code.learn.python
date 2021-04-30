# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 相对路径
project_dir = os.path.abspath('.')

path = project_dir + "\\pie.csv"
out_path = project_dir + "\\request_pie.jpg"

# 全路径
# path = "D:\\request.csv"
# out_path = "D:\\request.jpg"


def main():
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(path, encoding='utf-8')
    # 读取列名为距离误差和时间点的所有行数据
    label_list = data.loc[:, '月份']
    money_list = data.loc[:, '销售']

    # 设定各项距离圆心n个半径
    explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 饼状图
    plt.pie(money_list, explode=explode, labels=label_list, autopct='%1.1f%%', textprops={'fontsize': 43, 'color': 'k'}, shadow=None, startangle=90)
    # 显示图例
    plt.legend()
    # 统计图的标题
    plt.title(u"XX公司部门每月销售额", size=32)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(out_path)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
