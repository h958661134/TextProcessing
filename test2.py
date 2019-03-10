if __name__=="__main__":
    floor=[]
    for line in open("结果.txt"):
        string = ""
        k=['s','d','k']
        b=line.strip("\n,[,]")
        a=b.split("),")
        #print(len(a))
        #print(type(a))
        for w in k:
            print(w)