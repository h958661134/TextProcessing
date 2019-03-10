import sys
import jieba
import jieba.analyse
import xlrd

if __name__=="__main__":
    data = xlrd.open_workbook('现代汉语动词表.xls')
    rtable = data.sheets()[0]
    wordv=[]
    wordto=[]
    wordname=["柯镇恶","朱聪","韩小莹","韩宝驹","南希仁","全金发","张阿生"]
    for i in range(1,2084):
        if rtable.cell(i,0).value not in wordv:
            wordv.append(rtable.cell(i,0).value)

    for t in wordname:
        number0 = 0
        number1 = 0
        for line in open("结果2.txt"):
            if not line.find(t) == -1:
                if line.find("江南七怪") < line.find(t):
                    item0 = line[line.find("江南七怪"):line.find(t)]+t
                else:
                    item0 = line[line.find(t):line.find("江南七怪")]+"江南七怪"
                wordto.append(item0)
for x in wordto:
    print(x)