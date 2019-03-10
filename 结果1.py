import jieba
import sys
import jieba.analyse
import xlwt
import xlrd

if __name__=="__main__":
    wordname=[]
    for line in open("wordCount.txt"):
        item=line.strip('\n')
        wordname.append(item)
    with open("结果2.txt","w") as wf1:
        for line in open("结果1.txt"):
            s=0
            for t in wordname:
                if not line.find(t)==-1:
                    s=s+1
            if not s==0:
                wf1.write(line)
