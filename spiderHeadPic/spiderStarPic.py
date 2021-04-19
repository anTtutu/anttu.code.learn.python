# -*- coding:utf-8 -*-

import os
from icrawler.builtin import BingImageCrawler

# 根据人名爬取明星图，有很多误差，比如合照、签名图、艺名跟事务同名的(比如金星爬的都是星球)

# 相对路径
root_dir = os.path.abspath('.')

path = r'D:\Work\images'
fileName = "starFemaleName.txt"

f = open(fileName, 'r')
lines = f.readlines()
for i, line in enumerate(lines):
    name = line.strip('\n')
    file_path = os.path.join(path, name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    bing_storage = {'root_dir': file_path}
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4, storage=bing_storage)
    bing_crawler.crawl(keyword=name, max_num=10)
    print('第{}位明星：{}'.format(i, name))