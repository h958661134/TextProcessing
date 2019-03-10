import jieba
import sys
import jieba.analyse
import xlwt
import xlrd

if __name__=="__main__":
    wbk = xlwt.Workbook(encoding = 'ascii')  
    sheet = wbk.add_sheet("wordCount") 
    wordname=[]
    wordto0=[]
    stopwords=[]
    wordv=[]
    data = xlrd.open_workbook('现代汉语动词表.xls')
    rtable = data.sheets()[0]
    for i in range(1,2084):
        if rtable.cell(i,0).value not in wordto0:
            wordv.append(rtable.cell(i,0).value)
    for line in open("stop_words.txt"):
        item = line.strip('\n')
        stopwords.append(item)
    for line in open("wordCount.txt"):
        item=line.strip('\n')
        wordname.append(item)
    with open("自我剔除集柯镇恶.txt","w") as wf1:
        for line in open("射雕英雄传（世纪新修版）.txt"):
            if not line.find("江南七怪") == -1 and not line.find("柯镇恶") == -1:
                wf1.write(line)
    wf1.close()
    for line in open("自我剔除集柯镇恶.txt"):
        if(line.find("江南七怪")>line.find("柯镇恶")):
            item0=line[line.find("柯镇恶"):line.find("江南七怪")]
        else:
            item0=line[line.find("江南七怪"):line.find("柯镇恶")]
        item=item0.strip('\n\r').split('\t')
        tags = jieba.analyse.extract_tags(item[0])
        for t in tags:
            if t not in wordto0:
                if t not in wordname:
                    if t not in stopwords:
                        if t in wordv:
                            wordto0.append(t)
    with open("自我学习结果生成2.txt","w",encoding="GBK") as wf1:
        i=0
        for t in wordname:
            number0=0
            number1=0
            for line in open("结果2.txt"):
                if not line.find(t)==-1:
                    sign=0
                    for w in wordto0:
                        if not line.find(w)==-1:
                            if line.find("江南七怪")<line.find(t):
                                if not line[line.find("江南七怪"):line.find(t)].find(w)==-1:
                                    sign=sign+1
                                    break
                            else:
                                if not line[line.find(t):line.find("江南七怪")].find(w)==-1:
                                    sign=sign+1
                                    break
                    if sign==0:
                        number1=number1+1
                    else:
                        number0=number0+1
            sheet.write(i,0,t)
            sheet.write(i,1,str(number0))
            sheet.write(i,2,str(number1))
            sheet.write(i,3,str(number1/(number0*1.0+number1)))
            i=i+1
            wf1.write(t+" "+str(number0)+" "+str(number1)+" "+str(number0/(number0*1.0+number1))+"\n")
        wbk.save("自我学习.xls")
