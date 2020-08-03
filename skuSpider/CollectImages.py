# -*- coding:utf-8 -*-

# 引入requests包和正则表达式包re
import requests
import re
import xlrd
import os


# excel地址
# windows eg: E:\\WorkSpace\\vscode\\20190415092420.xls
# mac     eg: /Users/{whoami}/Downloads/skubarcode.xlsx
path = '/Users/{whoami}/Downloads/skubarcode.xlsx'

# 自定义下载页面函数
def load_page(url):
    response = requests.get(url)
    data = response.content
    return data

# 自定义保存页面图片函数
def get_image(html, sku, code):
    regx = r'https://[\S]+\.jpg'  # 定义图片正则表达式
    pattern = re.compile(regx)  # 编译表达式构造匹配模式
    get_images = re.findall(pattern, repr(html))  # 在页面中匹配图片链接

    #print('img url:%s' %get_images)

    savePath = './spider_picture/' + sku

    os.mkdir(savePath)

    num = 1
    num2 = 1
    # 遍历匹配成功的链接
    for img in get_images:
        #print('img url:%s' %img)

        if '100x100' in img:
            # 获取商品图的原图
            newImgUrl = img.replace('_100x100.jpg', '')
            print('sku img url: %s' %newImgUrl)
            # 根据图片链接，下载图片链接
            image = load_page(newImgUrl)
            # 转换编号格式
            index = str(num).rjust(2, '0')

            # 将下载的图片保存到对应的文件夹中
            with open(savePath + '/'+ code +'_z_%s.jpg' %index, 'wb') as fb:
                fb.write(image)
                print("正在下载商品图第%s张图片" %num)
                num = num + 1

        if 'ckeditor' in img:
            print('sku detail img url: %s' %img)
            # 转换编号格式
            index = str(num2).rjust(2, '0')

            # 根据图片链接，下载图片链接
            image = load_page(img)

            # 将下载的图片保存到对应的文件夹中
            with open(savePath + '/_m_%s.jpg' %index, 'wb') as fb:
                fb.write(image)
                print("正在下载描述图第%s张图片" %num2)
                num2 = num2 + 1

    print("下载%s完成！" %sku)

# 读取excel里面的料号和69码数据源
def read_xls(path):
    # 打开一个workbook
    workbook = xlrd.open_workbook(path)

    # 抓取所有sheet页的名称
    worksheets = workbook.sheet_names()
    print('worksheets is %s' % worksheets)

    # 定位到barcode
    worksheet1 = workbook.sheet_by_name(u'barcode')
    colsBarCode = worksheet1.col_values(0)  # 获取列内容
    print(colsBarCode)

    # 定位到SKU
    worksheet1 = workbook.sheet_by_name(u'SKU')
    colsSKU = worksheet1.col_values(0)  # 获取列内容
    print(colsSKU)

    return colsBarCode, colsSKU

def main():

    colsBarCode, colsSKU = read_xls(path)
    print('---------- baecode %s' %colsBarCode)
    print('---------- sku %s' %colsSKU)

    for sku in colsSKU:
        for barcode in colsBarCode:
            if sku in barcode:
                code = str(barcode).split(',', 1)[1]
                print('barcode: ' + str(barcode).split(',', 1)[1])
                print('sku:%s' %sku)

                menu = str(sku)[-3:]
                print('menu: ' + str(sku)[-3:])

                # 定义爬取页面的链接
                url = 'https://www.pct.com/detail/' + menu + '/'+ sku +'.html'
                print('url: %s' %url)

                # 调用load_page函数，下载页面内容
                html = load_page(url)

                # 在页面中，匹配图片链接，并将图片下载下来，保存到对应文件夹
                get_image(html, sku, code)

if __name__ == '__main__':
    main()