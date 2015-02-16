#函数，生成按index排序后的训练文件和预测文件
dic={}
def formatFile(lines,svmTrainFile):
    writeLine=''
    tempIndex=[]
    for line in lines:
        com=line.split(' ')
        writeLine+=com[0]
        i=1
        dic.clear()
        while i<len(com):
            index=int(com[i].split(':')[0])
            if not dic.has_key(index):
                dic.setdefault(index,1)
            else:
                count=dic.get(index)
                dic[index]=count+1
            tempIndex.append(index)
            i=i+1
        tempIndex.sort()
        for index in tempIndex:
            writeLine+=' '+str(index)+':'+str(dic.get(index))
        svmTrainFile.write(writeLine+'\n')
    svmTrainFile.flush()
    svmTrainFile.close()
#读取train并排序
path='G:\\CIKM2014\\CIKMData\\tempData\\removeDullData\\'
trainFile=open(path+'svmTrainInputFile','r')
lines=trainFile.readlines()
trainFile.close()
svmTrainFile=open(path+'svmTrain','w')
formatFile(lines,svmTrainFile)
#读取test并排序
testFile=open(path+'svmTestInputFile')
lines=testFile.readlines()
testFile.close()
svmTestFile=open(path+'svmTest','w')
formatFile(lines,svmTestFile)