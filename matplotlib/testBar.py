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

path = project_dir + "\\request.csv"
out_path = project_dir + "\\request_bar.jpg"

# 全路径
# path = "D:\\request.csv"
# out_path = "D:\\request.jpg"


def main():
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(path, encoding='gbk')
    # 读取列名为距离误差和时间点的所有行数据
    height_list = data.loc[:, 'error_count']
    name_list = data.loc[:, 'error_request_url']
    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 柱状图
    plt.bar(np.arange(len(name_list)), height_list, label=u'请求攻击统计', tick_label=name_list, fc='r')
    # 添加数据标签，也就是给柱子顶部添加标签
    x = np.arange(len(height_list))
    y = np.array(list(height_list.values))
    for a, b in zip(x, y):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    # 为了让x轴的内容适配展示的长度，请求路径字段比较长，有几十个字符
    plt.xticks(rotation=270)
    # 统计图的标题
    plt.title(u"请求攻击统计", size=20)
    # 显示图例
    plt.legend()
    # X坐标-横坐标标题
    plt.xlabel(u'请求名称', size=14)
    # Y坐标-纵坐标标题
    plt.ylabel(u'请求次数', size=14)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(out_path)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
