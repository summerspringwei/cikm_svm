def writeSvmFile(lines,svmFile,allWordDic):
    cl=["TEST","VIDEO", "NOVEL", "GAME", "TRAVEL", "LOTTERY", "ZIPCODE", "OTHER"]
    writeLine=''
    for line in lines:
        com=line.split('\t')
        label=0
        for i in range(8):
            if com[0].find(cl[i])!=-1:
                label=i
                writeLine=writeLine+str(i)
                break
        if len(com)>2:
            for w in (com[1]+" "+com[2]).split(' '):
                writeLine=writeLine+" "+str(allWordDic.get(w))+':1'
            svmFile.write(writeLine+'\n')
        writeLine=''
    svmFile.flush()
    svmFile.close()

import os
path='G:\\CIKM2014\\CIKMData\\tempData\\removeDullData\\'
os.chdir(path)
trainFile=open(path+'expandTrain','r')
testFile=open(path+'expandTest','r')
svmTrain=open(path+'svmTrain','w')
svmTest=open(path+'svmTest','w')
count=0
trainLines=trainFile.readlines()
testLines=testFile.readlines()
lines=trainLines+testLines
allWordDic={'0623665':1}
for line in lines:
    com=line.split('\t')
    words=com[1].split(' ')
    if len(com)>2:
        words=words+com[2].split(' ')
    for w in words:
        if w not in allWordDic:
            count=count+1
            allWordDic.setdefault(w,count)
print("dic Done")
trainFile.close()
testFile.close()
#上面为每个字编号
writeSvmFile(trainLines,svmTrain,allWordDic)
writeSvmFile(testLines,svmTest,allWordDic)
print('Done')
