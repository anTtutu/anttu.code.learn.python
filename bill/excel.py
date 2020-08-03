#coding=utf-8

import xlrd
import io
import sys
import re
import xlsxwriter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# excel所在目录，全路径
path='E:\\WorkSpace\\vscode\\发票信息20190415092420.xls'
out_path='E:\\WorkSpace\\vscode\\result.xlsx'

#打开一个workbook
workbook = xlrd.open_workbook(path)

#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

#定位到sheet1
worksheet1 = workbook.sheet_by_name(u'sheet1')

#获取列内容
rows = worksheet1.row_values(6)#获取行内容
cols = worksheet1.col_values(16)#获取列内容
#print(rows)
#print(cols)
n_rows = worksheet1.nrows
print('rows is %s' %n_rows)

warrantyNos=[rows]
batchNos=[rows]
operaters=[rows]

for i in range(n_rows):
    result_remark = worksheet1.cell_value(i, 16)
    print(result_remark)
    if '保单号' in result_remark:
        #print(result_remark)
        pat = re.compile('保单号:'+'(.*?)'+' 批单号', re.S)
        pat2 = re.compile('批单号:'+'(.*?)'+' 分期号', re.S)
        pat3 = re.compile('分期号:'+'(.*?)'+' 经办人', re.S)

        result1 = pat.findall(result_remark)
        result2 = pat2.findall(result_remark)
        result3 = pat3.findall(result_remark)

        #print(''.join(result1))      
        #print(''.join(result2))  
        #print(''.join(result3))

        warrantyNos.append(''.join(result1))
        batchNos.append(''.join(result2))
        operaters.append(''.join(result3))

#print('rows is %s' %len(warrantyNos))        

resultList=[]

for index in range(len(warrantyNos)):
    #print('index is %s' %index)
    if index == 0:
       continue
    warrantyNo = ''.join(warrantyNos[index])
    batchNo = ''.join(batchNos[index])
    operater = ''.join(operaters[index])

    #print('warrantyNo is %s' %warrantyNo)
    #print('batchNo is %s' %batchNo)
    #print('operater is %s' %operater)

    str2 = batchNo.replace('等', '')
    str3 = operater.replace('等', '')

    if batchNo == '':
        result = warrantyNo+'0'+str3    
        print(result)
    else:
        result = str2+'0'+str3    
        print(result)

    resultList.append(result)

    # 创建工作簿
    workbook = xlsxwriter.Workbook(out_path) #创建工作簿
    # 创建sheet
    worksheet = workbook.add_worksheet(u'结果')
    # 设置第一列20高度
    worksheet.set_column('A:A',20)
    
    worksheet.write_column('A1', resultList)

    workbook.close()

print('-----OK-----')