# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Description    :  
@Author         :  Anttu
@Version        :  v1.0
@File           :  getFont2Mac.py
@CreateTime     :  30/4/2021 22:36
"""
import subprocess

import matplotlib.font_manager as fm

fm = fm.FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
# print( '*' * 10, '系统可用的中文字体', '*' * 10)
# print (output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
available = mat_fonts & zh_fonts
print('*' * 10, '可用的字体', '*' * 10)
for f in available:
    print(f)
