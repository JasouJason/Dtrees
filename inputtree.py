import sys
sys.path.append('G:\\desktop\\dataset')
import tryplo

f= open('temp1.txt','r')  
a1= f.read()  
trid31= eval(a1)  
f.close()  
c1=tryplo.getNumLeafs(trid31)
d1=tryplo.getTreeDepth(trid31)

f=open('temp2.txt','r')  
a2=f.read()  
trid32=eval(a2)  
f.close()  
c2=tryplo.getNumLeafs(trid32)
d2=tryplo.getTreeDepth(trid32)

f=open('temp3.txt','r')  
a3=f.read()  
trid33=eval(a3)  
f.close()  
c3=tryplo.getNumLeafs(trid33)
d3=tryplo.getTreeDepth(trid33)

f=open('temp4.txt','r')  
a4=f.read()  
trid34=eval(a4)  
f.close()  
c4=tryplo.getNumLeafs(trid34)
d4=tryplo.getTreeDepth(trid34)

f=open('temp5.txt','r')  
a5=f.read()  
trid35=eval(a5)  
f.close() 
c5=tryplo.getNumLeafs(trid35)
d5=tryplo.getTreeDepth(trid35) 

f=open('temp6.txt','r')  
a6=f.read()  
trid36=eval(a6)  
f.close()  
c6=tryplo.getNumLeafs(trid36)

f=open('temp7.txt','r')  
a7=f.read()  
trid37=eval(a7)  
f.close()  
c7=tryplo.getNumLeafs(trid37)
d7=tryplo.getTreeDepth(trid37)

f=open('temp8.txt','r')  
a8=f.read()  
trid38=eval(a8)  
f.close()  
c8=tryplo.getNumLeafs(trid38)
d8=tryplo.getTreeDepth(trid38)

f=open('temp9.txt','r')  
a9=f.read()  
trid39=eval(a9)  
f.close()  
c9=tryplo.getNumLeafs(trid39)
d9=tryplo.getTreeDepth(trid39)

f=open('temp10.txt','r')  
a10=f.read()  
trid310=eval(a10)  
f.close()
c10=tryplo.getNumLeafs(trid310)
d10=tryplo.getTreeDepth(trid310)

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
e10=tryplo.getNumLeafs(trc4510)
f10=tryplo.getTreeDepth(trc4510)

numleafid3=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
numdepthid3=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

numleafc45=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
numdepthc45=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

