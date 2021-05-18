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
fileName = "stack.csv"
outFileName = "request_stack_bar.jpg"

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
plt.rcParams['axes.labelsize'] = 32
plt.rcParams['xtick.labelsize'] = 24
plt.rcParams['ytick.labelsize'] = 24
plt.rcParams['legend.fontsize'] = 20

filePath = os.sep.join([project_dir, fileName])
outPath = os.sep.join([project_dir, outFileName])

# 全路径
# filePath = "D:\\request.csv"
# outPath = "D:\\request.jpg"


def main():
    # 使用python下pandas库读取csv文件
    data = pd.read_csv(filePath, encoding='utf-8')
    # 读取列名为距离误差和时间点的所有行数据
    name_list = data.loc[:, '姓名']
    january_list = data.loc[:, '一月']
    february_list = data.loc[:, '二月']
    march_list = data.loc[:, '三月']
    april_list = data.loc[:, '四月']
    may_list = data.loc[:, '五月']
    june_list = data.loc[:, '六月']
    july_list = data.loc[:, '七月']
    august_list = data.loc[:, '八月']
    september_list = data.loc[:, '九月']
    october_list = data.loc[:, '十月']
    november_list = data.loc[:, '十一月']
    december_list = data.loc[:, '十二月']
    # 设置画布
    plt.figure(num=1, dpi=100, figsize=(24, 32))
    # 堆积柱状图
    plt.bar(np.arange(len(name_list)), january_list, label=u'1月业绩', tick_label=name_list, fc='r')
    plt.bar(np.arange(len(name_list)), february_list, label=u'2月业绩', bottom=january_list, tick_label=name_list, fc='b')
    plt.bar(np.arange(len(name_list)), march_list, label=u'3月业绩', bottom=january_list+february_list, tick_label=name_list, fc='g')
    plt.bar(np.arange(len(name_list)), april_list, label=u'4月业绩', bottom=january_list+february_list+march_list, tick_label=name_list, fc='c')
    plt.bar(np.arange(len(name_list)), may_list, label=u'5月业绩', bottom=january_list+february_list+march_list+april_list, tick_label=name_list, fc='y')
    plt.bar(np.arange(len(name_list)), june_list, label=u'6月业绩', bottom=january_list+february_list+march_list+april_list+may_list, tick_label=name_list, fc='m')
    plt.bar(np.arange(len(name_list)), july_list, label=u'7月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list, tick_label=name_list, fc='WhiteSmoke')
    plt.bar(np.arange(len(name_list)), august_list, label=u'8月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list+july_list, tick_label=name_list, fc='pink')
    plt.bar(np.arange(len(name_list)), september_list, label=u'9月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list, tick_label=name_list, fc='olive')
    plt.bar(np.arange(len(name_list)), october_list, label=u'10月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list, tick_label=name_list, fc='navy')
    plt.bar(np.arange(len(name_list)), november_list, label=u'11月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list+october_list, tick_label=name_list, fc='linen')
    plt.bar(np.arange(len(name_list)), december_list, label=u'12月业绩', bottom=january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list+october_list+november_list, tick_label=name_list, fc='teal')
    # 添加数据标签，也就是给柱子顶部添加标签
    x = np.arange(len(name_list))
    y1 = np.array(list(january_list.values))
    for a, b in zip(x, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y2 = np.array(list((january_list+february_list).values))
    for a, b in zip(x, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y3 = np.array(list((january_list+february_list+march_list).values))
    for a, b in zip(x, y3):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y4 = np.array(list((january_list+february_list+march_list+april_list).values))
    for a, b in zip(x, y4):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y5 = np.array(list((january_list+february_list+march_list+april_list+may_list).values))
    for a, b in zip(x, y5):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y6 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list).values))
    for a, b in zip(x, y6):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y7 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list).values))
    for a, b in zip(x, y7):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y8 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list).values))
    for a, b in zip(x, y8):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y9 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list).values))
    for a, b in zip(x, y9):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y10 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list+october_list).values))
    for a, b in zip(x, y10):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y11 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list+october_list+november_list).values))
    for a, b in zip(x, y11):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24)

    y12 = np.array(list((january_list+february_list+march_list+april_list+may_list+june_list+july_list+august_list+september_list+october_list+november_list+december_list).values))
    for a, b in zip(x, y12):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=24, color='AliceBlue')
    # x轴的字段
    plt.xticks(np.arange(len(name_list)), name_list)
    # 统计图的标题
    plt.title(u"XX公司部门每月销售额", size=32)
    # 显示图例
    plt.legend()
    # X坐标-横坐标标题
    plt.xlabel(u'部门名称', size=24)
    # Y坐标-纵坐标标题
    plt.ylabel(u'销售额', size=24)
    # 在展示图片前可以将画出的曲线保存到自己路径下的文件夹中
    plt.savefig(outPath)
    # 显示图像
    plt.show()
    print("all picture is starting")


if __name__ == "__main__":
    main()
