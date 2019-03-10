import jieba
import sys

if __name__=="__main__":
    with open("自我剔除集丘处机.txt","w") as wf1:
        for line in open("射雕英雄传（世纪新修版）.txt"):
            if not line.find("江南七怪") == -1 and not line.find("丘处机") == -1:
                wf1.write(line)
    with open("自我剔除集郭靖.txt","w",encoding="GBK") as wf1:
        for line in open("射雕英雄传（世纪新修版）.txt"):
            if not line.find("江南七怪") == -1 and not line.find("郭靖") == -1:
                wf1.write(line)
