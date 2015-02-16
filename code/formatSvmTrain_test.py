
path='G:\\CIKM2014\\CIKMData\\tempData\\removeDullData\\'
trainFile=open(path+'expandTrain','r')
cl=["VIDEO", "NOVEL", "GAME", "TRAVEL", "LOTTERY", "ZIPCODE", "OTHER"]

trainWordDic={}
lines=trainFile.readlines()
count=0
for line in lines:
    com=line.split('\t')
    if len(com)>2:
        words=(com[1]+' '+com[2]).split(' ')
        for word in words:
            if not trainWordDic.has_key(word):
                count+=1
                trainWordDic[word]=count
trainFile.close()
print('Before - trainWordDic size:'+str(len(trainWordDic)))


testFile=open(path+'expandTest')
testWordDic={}
lines=testFile.readlines()
count=0
for line in lines:
    com=line.split('\t')
    if len(com)>2:
        words=(com[1]+' '+com[2]).split(' ')
        for word in words:
            if not testWordDic.has_key(word):
                count+=1
                testWordDic[word]=count;
testFile.close()
print('testWordDic Size:'+str(len(testWordDic)))


for key in trainWordDic.keys():
    if not testWordDic.has_key(key):
        trainWordDic.pop(key)
print('After - trainWordDic size:'+str(len(trainWordDic)))

#重新编码
count=1
for key in trainWordDic.keys():
    trainWordDic[key]=count
    count+=1

#开始生成train文件
print('start write')
trainFile=open(path+'expandTrain','r')
lines=trainFile.readlines()
trainFile.close()
svmTrainWriteFile=open(path+'libSvmTrainInputFile','w')
svmTrainLine=''
print('lines '+str(len(lines)))
count=0
for line in lines:
    com=line.split('\t')
    for c in range(len(cl)):
        if com[0].find(cl[c])!=-1 and len(com)>2:
            svmTrainLine+=str(c)
            words=(com[1]+' '+com[2]).split(' ')
            for w in words:
                if trainWordDic.has_key(w):
                    svmTrainLine+=' '+str(trainWordDic.get(w))+':'+'1'
            svmTrainLine+='\n'
            svmTrainWriteFile.write(svmTrainLine)
            count+=1
            if count%1000==0:
                print(str(count)+'\t'+svmTrainLine)
            svmTrainLine=''
svmTrainWriteFile.flush()
svmTrainWriteFile.close()
print('Done')

#生成test
testFile=open(path+'expandTest','r')
lines=testFile.readlines()
testFile.close()
print('start test write')
svmTestWriteFile=open(path+'svmTestInputFile','w')
svmTestLine=''
for line in lines:
    com=line.split('\t')
    if len(com)>2:
        words=(com[1]+' '+com[2]).split(' ')
        svmTestLine+='0'
        for w in words:
            if trainWordDic.has_key(w):
                svmTestLine+=' '+str(trainWordDic.get(w))+':'+'1'
        svmTestLine+='\n'
        svmTestWriteFile.write(svmTestLine)
        svmTestLine=''
svmTestWriteFile.flush()
svmTestWriteFile.close()