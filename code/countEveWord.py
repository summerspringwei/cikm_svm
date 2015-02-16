path='G:\\CIKM2014\\CIKMData\svm\\libsvm\\windows\\data\\'
trainFile=open(path+'svmTrain','r')
wordDic=[{'0000000':1},{'0000000':1},{'0000000':1},{'0000000':1},{'0000000':1},{'0000000':1},{'0000000':1},{'0000000':1}]
totalDic={'0000000':1}
lines=trainFile.readlines()
for line in lines:
    com=line.split(' ')
    label=int(com[0])
    for w in com:
        if not wordDic[label-1].has_key(w):
            wordDic[label].setdefault(w,1)
        if not totalDic.has_key(w):
            totalDic.setdefault(w,1)
for i in range(len(wordDic)):
    print('class '+str(i)+':'+str(len(wordDic[i]))+'\n')
print('total word:'+str(len(totalDic)))