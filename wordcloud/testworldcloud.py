# -*- coding:utf-8 -*-

import wordcloud
import jieba
from imageio import imread
import os

# 相对路径
root_dir = os.path.abspath('.')
background_path = root_dir + "\\background\\star.png"
word_path = root_dir + "\\word\\safe.txt"

# 词云的背景图案
mask = imread(background_path)
# 词云的词汇
f = open(word_path, "r", encoding="utf-8")
t = f.read()
f.close()
# 拆词
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white", mask=mask)

# 生成词云：字体微软雅黑，宽1000，高度700，背景白色
w.generate(txt)
w.to_file("demo2.png")