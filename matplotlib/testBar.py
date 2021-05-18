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
fileName = "request.csv"
outFileName = "request_bar.jpg"

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
    data = pd.read_csv(filePath, encoding='gbk')
    # 读取列名
    height_list = data.loc[:, 'error_count']
    name_list = data.loc[:, 'error_request_url']
    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 柱状图
    plt.bar(np.arange(len(name_list)), height_list, label=u'请求攻击统计', tick_label=name_list, fc='turquoise')
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
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
