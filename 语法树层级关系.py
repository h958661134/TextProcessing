import sys
import xlwt
import xlrd

if __name__=="__main__":
    floor=[]
    with open("test.txt","w",encoding="GBK") as wf1:
        for line in open("out.txt"):
            string = ""
            item=line.strip("\n,[,],")
            b=item.split("),")
            for k1 in b:
                k=k1.strip(" ")
                if k[0] == "n" or k[0:4]=="assm":
                    string=string+" "+k[k.find("(")+1:k.find("-")]
            wf1.write(string+"\n")
