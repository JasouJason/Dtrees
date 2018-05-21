#计算给定数据集的香农熵
import sys
import math
import random as rd
import numpy as np
import pandas as pd
sys.path.append('G:\\desktop\\dataset')
import treesc45
# =============================================================================
# 弄好数据格式，分数据集以及标签
# =============================================================================
#读取数据
bank_data=pd.read_table('G:\\desktop\\dataset\\bank-additional-full.csv',sep=';')

#标签
labels=bank_data.keys().tolist()
labels1=bank_data.keys().tolist()

#训练集以及测试集

#temp_data=np.array(bank_data[2000:])
#dataSet=temp_data.tolist()
rd.seed(10)
numdata=len(bank_data)
num=10
num_unit=math.floor(numdata/num)

arr=np.arange(numdata-1)
rd.shuffle(arr)

sortdata=list(arr)


temp_data=np.array(bank_data)
dataSet=temp_data.tolist()
list_t=[]
list_k=[]
list_p=[]
list_g=[]


i=9

a=sortdata[i*num_unit:(i+1)*num_unit]
b=sortdata[:i*num_unit]+sortdata[(i+1)*num_unit:]
testdata=[]
testdata1=[]
traindata=[]
result=[]

for jj in a:
    testdata1.append(dataSet[jj])
for kk in b:
    traindata.append(dataSet[kk])
    
    
numFeas=len(testdata1[0])-1
result=[example[-1] for example in testdata1]
for tt in testdata1:
    testdata.append(tt[:numFeas])
myTree={}
myTree=treesc45.createTree(traindata,labels)

def getNumleafs(myTree):
    numLeafs=0
    firstSides = list(myTree.keys()) 
    firstStr = firstSides[0]#找到输入的第一个元素
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key])==dict:
            numLeafs+=getNumleafs(secondDict[key])
        else:   numLeafs+=1
    return numLeafs

#树的层数
def getTreeDepth(myTree):
    maxDepth=0
    firstSide=list(myTree.keys())
    firstStr=firstSide[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key])==dict:
            thisDepth=1+getTreeDepth(secondDict[key])
        else:   thisDepth=1
        if thisDepth>maxDepth:   maxDepth=thisDepth
    return maxDepth
a=getNumleafs(myTree)
b=getTreeDepth(myTree)


num_testd=len(testdata)
classify1=[0]*num_testd
k=0
g=0
p=0
t=0
for ii in range(num_testd):
    try:
        classify1[ii]=treesc45.classify(myTree,labels1,testdata[ii])
        if classify1[ii]==result[ii]:
           k=k+1
    except:
        g=g+1
t=k/(num_testd-g)
p=g/num_testd

#导出所得决策树
#f = open('c4510.txt','w')  
#f.write(str(myTree))  
#f.close()  
