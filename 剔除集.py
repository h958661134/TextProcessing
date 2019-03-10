import jieba
import sys
import jieba.analyse
import xlwt
import xlrd

if __name__=="__main__":
    wordto0=[]
    for line in open("自我剔除集郭靖.txt"):
        if(line.find("江南七怪")>line.find("郭靖")):
            item0=line[line.find("郭靖"):line.find("江南七怪")]
        else:
            item0=line[line.find("江南七怪"):line.find("郭靖")]
        item=item0.strip('\n\r').split('\t')
        tags = jieba.analyse.extract_tags(item[0])
        for t in tags:
            if t not in wordto0:
                wordto0.append(t)
    for line in open("自我剔除集丘处机.txt"):
        if(line.find("江南七怪")>line.find("丘处机")):
            item0=line[line.find("丘处机"):line.find("江南七怪")]
        else:
            item0=line[line.find("江南七怪"):line.find("丘处机")]
        item=item0.strip('\n\r').split('\t')
        tags = jieba.analyse.extract_tags(item[0])
        for t in tags:
            if t not in wordto0:
                wordto0.append(t)
    for line in open("结果.txt"):
        sign=0
        for w in wordto0:
            if line.find("江南七怪")<line.find("丘处机"):
                if not line[line.find("江南七怪"):line.find("丘处机")].find(w)==-1:
                    sign=sign+1
                    break
            else:
                if not line[line.find("丘处机"):line.find("江南七怪")].find(w)==-1:
                    sign=sign+1
                    break
        if sign==0:
            print(line[line.find("江南七怪"):line.find("丘处机")])
                
                
