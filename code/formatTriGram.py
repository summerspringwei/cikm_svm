#tri-gram 形成每一类的三个字连在一起的词的集合，并统计出现次数的次数
#如果triTerm没有在Test中出现过，就去掉，这样triTerm的数量大约降低到原来的1/3
#七类的词典，并分别写到文件中
path='G:\\CIKM2014\\CIKMData\\tempData\\removeDullData\\'
trainFile=open(path+'expandTrain','r')
cl=["VIDEO", "NOVEL", "GAME", "TRAVEL", "LOTTERY", "ZIPCODE", "OTHER"]
clDic=[{"1000000":1},{"1000000":1},{"1000000":1},{"1000000":1},{"1000000":1},{"1000000":1},{"1000000":1}]
lines=trainFile.readlines()
for line in lines:
    com=line.split('\t')
    for c in range(len(cl)):
        if com[0].find(cl[c])!=-1:
            if len(com)>2:
                words=(com[1]+' '+com[2]).split(' ')
                for i in range(len(words)-2):
                    triTerm=words[i]+' '+words[i+1]+' '+words[i+2]
                    if clDic[c].has_key(triTerm):
                        clDic[c][triTerm]=clDic[c][triTerm]+1
                    else:
                        clDic[c].setdefault(triTerm,1)
print('format dic done!')

#输出每一类的单词量
print('before')
for i in range(len(clDic)):
    print('class :'+str(cl[i])+'Times:'+str(len(clDic[i])))

#test的词典
testFile=open(path+'expandTest')
testDic={}
lines=testFile.readlines()
for line in lines:
    com=line.split('\t')
    if len(com)>2:
        words=(com[1]+com[2]).split(' ')
        for i in range(len(words)-2):
            triTerm=words[i]+' '+words[i+1]+' '+words[i+2]
            if testDic.has_key(triTerm):
                testDic[triTerm]=testDic[triTerm]+1
            else:
                testDic.setdefault(triTerm,1)

#遍历这七类的词典，如果词在test中没有出现过，就删除掉

print('testDic size:'+str(len(testDic)))
for c in range(len(clDic)):
    for key in clDic[c].keys():
        if not testDic.has_key(key):
            clDic[c].pop(key)

#输出每一类的单词量
print('after')
for i in range(len(clDic)):
    print('class :'+str(cl[i])+'Times:'+str(len(clDic[i])))

#写到文件中
"""
line=''
triTermTime={}
for i in range(len(cl)):
    clDic[i].pop('1000000')
    trainDic=open(path+cl[i],'w')
    for (key,value) in clDic[i].iteritems():
        line=key+':'+str(value)+'\n'
        trainDic.write(line)
        if not triTermTime.has_key(value):
            triTermTime.setdefault(value,1)
        else:
            count=triTermTime.get(value)
            count=count+1
            triTermTime[value]=count
    line=''
    trainDic.flush()
    trainDic.close()
    print(cl[i]+' done!\n')

"""