# -*- coding:utf-8 -*-

import os
import csv  # 导入csv模块，该模块包含于python标准库中
from matplotlib import pyplot as plt  # 从matplotlib中导入pyplot并重命名为plt
from pylab import *
import platform

# 系统
print(platform.system())

# 相对路径
project_dir = os.path.abspath('.')
print(project_dir)
fileName = "request.csv"
outFileName = "request_line.jpg"

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
mpl.rcParams['font.sans-serif'] = fontName
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

filePath = os.sep.join([project_dir, fileName])
outPath = os.sep.join([project_dir, outFileName])

# 全路径
# filePath = "D:\\request.csv"
# outPath = "D:\\request.jpg"


def main():
    with open(filePath) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # 提取请求次数、请求名数据存储在列表中
        counts, requests = [], []
        for row in reader:
            # 请求次数
            count = int(row[0])
            counts.append(count)

            # 请求路径
            request = str(row[1])
            requests.append(request)

    # 绘制图表
    plt.figure(dpi=100, figsize=(24, 32))   # 添加绘图窗口，可绘制多条曲线
    plt.plot(requests, counts, marker='*', c='red', alpha=0.6)  # plot()函数，第一个参数x值，第二个y值
    # ax = plt.gca()  # 获得当前axis
    # bottom, top = plt.ylim()  # 获得y轴最大最小值
    # ax.spines['bottom'].set_position(('data', bottom)) # 移动x轴到y轴最小值位置
    # 添加数据标签，也就是给柱子顶部添加标签
    x = np.arange(len(requests))
    y = np.array(list(counts))
    for a, b in zip(x, y):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    # 设置图形的格式
    plt.title("请求攻击次数", fontsize=20)   # 图形标题
    plt.xlabel("请求路径", fontsize=14)   # x轴标题及字号
    plt.ylabel("请求次数", fontsize=14)   # y轴标题及字号
    plt.tick_params(axis='both', which='major', labelsize=8)  # 坐标轴格式
    # 为了让x轴的内容适配展示的长度，请求路径字段比较长，有几十个字符
    plt.xticks(rotation=270)
    # 给图表区域着色
    plt.fill_between(requests, counts, facecolor='blue', alpha=0.1)
    """
    facecolor为填充区域颜色
    alpha为填充颜色的透明度，0表示完全透明，1表示完全不透明
    """
    # 将图片保存到指定目录
    plt.savefig(outPath)
    # 显示图表
    plt.show()


if __name__ == "__main__":
    main()
