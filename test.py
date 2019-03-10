import sys

if __name__=="__main__":
    wordname = ["柯镇恶", "朱聪", "韩小莹", "韩宝驹", "南希仁", "全金发", "张阿生"]
    with open("江南七怪.txt","w",encoding="GBK") as tt:
        for x in wordname:
            tt.write(x+"文段：\n\n")
            for line in open("射雕英雄传（世纪新修版）.txt"):
                if not line.find(x)==-1:
                    tt.write(line)
            tt.write("\n\n\n")