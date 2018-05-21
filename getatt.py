import sys
sys.path.append('G:\\desktop\\dataset')
import tryplo
f=open('c451.txt','r')  
b1=f.read()  
trc451=eval(b1)  
f.close()
e1=tryplo.getNumLeafs(trc451)
f1=tryplo.getTreeDepth(trc451)

f=open('c452.txt','r')  
b2=f.read()  
trc452=eval(b2)  
f.close()  
e2=tryplo.getNumLeafs(trc452)
f2=tryplo.getTreeDepth(trc452)

f=open('c453.txt','r')  
b3=f.read()  
trc453=eval(b3)  
f.close()  
e3=tryplo.getNumLeafs(trc453)
f3=tryplo.getTreeDepth(trc453)

f=open('c454.txt','r')  
b4=f.read()  
trc454=eval(b4)  
f.close()  
e4=tryplo.getNumLeafs(trc454)
f4=tryplo.getTreeDepth(trc454)

f=open('c455.txt','r')  
b5=f.read()  
trc455=eval(b5)  
f.close()  
e5=tryplo.getNumLeafs(trc455)
f5=tryplo.getTreeDepth(trc455)

f=open('c456.txt','r')  
b6=f.read()  
trc456=eval(b6)  
f.close()  
e6=tryplo.getNumLeafs(trc456)
f6=tryplo.getTreeDepth(trc456)

f=open('c457.txt','r')  
b7=f.read()  
trc457=eval(b7)  
f.close()  
e7=tryplo.getNumLeafs(trc457)
f7=tryplo.getTreeDepth(trc457)

f=open('c458.txt','r')  
b8=f.read()  
trc458=eval(b8)  
f.close()  
e8=tryplo.getNumLeafs(trc458)
f8=tryplo.getTreeDepth(trc458)

f=open('c459.txt','r')  
b9=f.read()  
trc459=eval(b9)  
f.close()  
e9=tryplo.getNumLeafs(trc459)
f9=tryplo.getTreeDepth(trc459)

f=open('c4510.txt','r')  
b10=f.read()  
trc4510=eval(b10)  
f.close()  

def resu_att1(myTree):
    firstSide=list(myTree.keys())
    firstStr=firstSide[0]
    secondDict=myTree[firstStr]
    num1=[]
    num2=[]
    num3=[]
    num4=[]
    num5=[]
    num6=[]
    for key1 in secondDict.keys():
        if type(secondDict[key1])==dict:
            secondSide=list(secondDict[key1].keys())
            secondStr=secondSide[0]
            num1.append(secondStr)
            thirdDict=secondDict[key1][secondStr]
            for key2 in thirdDict.keys():
                if type(thirdDict[key2])==dict:
                    thirdSide=list(thirdDict[key2].keys())
                    thirdStr=thirdSide[0]
                    num2.append(thirdStr)
                    fourthDict=thirdDict[key2][thirdStr]
                    for key3 in fourthDict.keys():
                        if type(fourthDict[key3])==dict:
                            fourthSide=list(fourthDict[key3].keys())
                            fourthStr=fourthSide[0]
                            num3.append(fourthStr)
                            fifthDict=fourthDict[key3][fourthStr]
                            for key4 in fifthDict.keys():
                                if type(fifthDict[key4])==dict:
                                    fifthSide=list(fifthDict[key4].keys())
                                    fifthStr=fifthSide[0]
                                    num4.append(fifthStr)
                                    sixthDict=fifthDict[key4][fifthStr]
                                    for key5 in sixthDict.keys():
                                        if type(sixthDict[key5])==dict:
                                            sixthSide=list(sixthDict[key5].keys())
                                            sixthStr=sixthSide[0]
                                            num5.append(sixthStr)
                                            seventhDict=sixthDict[key5][sixthStr]
                                            for key6 in seventhDict.keys():
                                                if type(seventhDict[key6])==dict:
                                                    seventhSide=list(seventhDict[key6].keys())
                                                    seventhStr=seventhSide[0]
                                                    num6.append(seventhStr)
    return num1,num2,num3,num4,num5,num6

are1,bre1,cre1,dre1,ere1,fre1=resu_att1(trc451)
are2,bre2,cre2,dre2,ere2,fre2=resu_att1(trc452)
are3,bre3,cre3,dre3,ere3,fre3=resu_att1(trc453)
are4,bre4,cre4,dre4,ere4,fre4=resu_att1(trc454)
are5,bre5,cre5,dre5,ere5,fre5=resu_att1(trc455)
are6,bre6,cre6,dre6,ere6,fre6=resu_att1(trc456)
are7,bre7,cre7,dre7,ere7,fre7=resu_att1(trc457)
are8,bre8,cre8,dre8,ere8,fre8=resu_att1(trc458)
are9,bre9,cre9,dre9,ere9,fre9=resu_att1(trc459)
are10,bre10,cre10,dre10,ere10,fre10=resu_att1(trc4510)

def numuniatt(list111):
    b={}
    uniatt=set(list111)
    for att in uniatt:
        b[att]=list111.count(att)
    return b

kf1=numuniatt(are1)
kf2=numuniatt(are2)
kf3=numuniatt(are3)
kf4=numuniatt(are4)
kf5=numuniatt(are5)
kf6=numuniatt(are6)
kf7=numuniatt(are7)
kf8=numuniatt(are8)
kf9=numuniatt(are9)
kf10=numuniatt(are10)

kc1=numuniatt(bre1)
kc2=numuniatt(bre2)
