#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: 样例代码.py
@time: 2018/4/6 13:29
'''
import codecs
import numpy as np
import jieba
from tqdm import tqdm

lines=codecs.open('射雕英雄传（世纪新修版）.txt').read().split('\n')
id2sent=dict(enumerate(lines))
word2sentid={}
tf={}

for i in tqdm(iter(range(len(lines)-1))):
    for w in set(jieba.cut(lines[i]+lines[i+1],HMM=False)):
        if w not in word2sentid:
            word2sentid[w]=[]
        if w not in tf:
            tf[w]=0
        word2sentid[w].append(i)
        tf[w]+=1

total=sum(tf.values())*1.0
idf = {i:np.log(total)-np.log(j) for i,j in tf.items()}

def answers(s):
    ws = jieba.lcut(s,HMM=False)
    result={}
    for w in ws:
        for i in word2sentid.get(w,[]):
            if i not in result:
                try:
                    result[i]=0
                except:
                    pass
            try:
                result[i]+=idf[w]
            except:
                pass
    i1=list(result.keys())
    i = i1[np.argmax(result.values())]
    return(id2sent[i]+'\n'+id2sent[i+1])

print(answers('江南七怪分别是谁'))
print(answers('九阴真经是谁写的'))

