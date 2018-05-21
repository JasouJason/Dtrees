#计算给定数据集的香农熵
from math import log

import numpy as np
import pandas as pd
bank_data=pd.read_table('G:\\desktop\\dataset\\bank-additional-full.csv',sep=';')

#数据集以及属性
labels=bank_data.keys().tolist()
labels1=bank_data.keys().tolist()
temp_data=np.array(bank_data[:4000])
dataSet=temp_data.tolist()


def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVex in dataSet:
        currentLabel=featVex[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt


#划分数据集
def splitDataSet(dataSet,axis,value):
#数据集，属性，想挑选属性的值
    retDataSet=[]
#创建列表
    for featVec in dataSet:
        if  featVec[axis]==value:
#索引属性是否等于所挑选的值
            reducedFeatVec=featVec[:axis]
#获得该行数据属性前的数据
            reducedFeatVec.extend(featVec[axis+1:])
#加入属性后的数据
            retDataSet.append(reducedFeatVec)
#写入列表
    return retDataSet


#选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
#未分裂香农熵
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature=-1
#属性分开
    for i in range(numFeatures):
#得到某列某属性的全部数据
        feaList=[example[i] for example in dataSet]
#去重
        uniqueVals=set(feaList)
        newEntropy=0.0
        splitInfo=1.0
        for value in uniqueVals:
#遍历属性
            subDataSet=splitDataSet(dataSet,i,value)
#某属性集合
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
            splitInfo-=prob*log(prob,2)
        infoGain=(baseEntropy-newEntropy)/splitInfo
#某属性的信息增益
        if(infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
#比较各属性信息增益的大小，保存最大属性的位置
    return bestFeature


import operator
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet,labels):
#最后一列
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
#最后一列第一项等于该列表的数量，及都为统一项
    if len(dataSet[0])==1:
        return majorityCnt(classList)
#列表

    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]  #最优属性

    myTree={bestFeatLabel:{}}  #创建最优属性的树
#去除最优属性
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
        #最优属性的分类，递归，将一支走到底
    return myTree

myTree=createTree(dataSet,labels)

#叶节点的数目
def getNumleafs(myTree):
    numLeafs=0
    firstSides=list(myTree.keys()) 
    firstStr=firstSides[0]#找到输入的第一个元素
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

testdata=bank_data[4000:]
result=list(testdata['y'])
testdata=testdata.drop('y',1)
temp_testVec=np.array(testdata)
testVec=temp_testVec.tolist()


def classify(inputTree,featLabels,testVec):
    firstside=list(inputTree.keys())
    firstStr=firstside[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key])==dict:
                classLabel=classify(secondDict[key],featLabels,testVec)
            else:
                classLabel=secondDict[key]
    return classLabel
#没有说到做到,同时我认识到另一种看待问题的方式，以及一直以来的心病，这将是我人生中的重大财富
#还有持续性
#classify(myTree,labels,[1,0])
#classify(myTree,labels,[1,1])
num_testd=len(testVec)
classify1=[0]*num_testd
k=0
g=0
for i in range(num_testd):
    try:
        classify1[i]=classify(myTree,labels1,testVec[i])
        if classify1[i]==result[i]:
           k=k+1
    except:
        g=g+1
t=k/(num_testd-g)
p=g/num_testd
