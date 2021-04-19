# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 相对路径
project_dir = os.path.abspath('.')

path = project_dir + "\\request.csv"
out_path = project_dir + "\\request.jpg"

# 全路径
# path = "D:\\request.csv"
# out_path = "D:\\request.jpg"

def main():
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(path, encoding='gbk')
    # 距离误差
    # 读取列名为距离误差和时间点的所有行数据
    y_data = data.loc[:, 'error_count']
    x_data = data.loc[:, 'error_request_url']
    # 读取列名为距离误差的前1000行数据
    # y_data = data.loc[:1000,'距离误差']
    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 点线图
    plt.plot(x_data, y_data, '*-', label=u'请求攻击统计', linewidth=1)
    plt.xticks(rotation=270)
    # 统计图的标题
    plt.title(u"请求攻击统计", size=20)
    plt.legend()
    # X坐标-横坐标标题
    plt.xlabel(u'请求名称', size=14)
    # Y坐标-纵坐标标题
    plt.ylabel(u'请求次数', size=14)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(out_path)
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
