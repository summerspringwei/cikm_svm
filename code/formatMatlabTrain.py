def formatMatlabFile(lines,matlabFile):
    countLine=1
    writeLine=''
    for line in lines:
        com=line.split(' ')
        writeLine=writeLine+str(countLine)+' 1 '+str(com[0])+'\n'
        for w in com:
            writeLine=writeLine+str(countLine)+' '+str(int(w.split(':')[0])+1)+' 1\n'
        matlabFile.write(writeLine)
        writeLine=''
        countLine=countLine+1
    matlabFile.flush()
    matlabFile.close()
    
print('format matlab file start')
path='G:\\CIKM2014\\CIKMData\\svm\\libsvm\\java\\data\\'
svmTrainFile=open(path+'svmTrain','r')
svmTestFile=open(path+'svmTest','r')
matlabTrain=open(path+'matlabTrain','w')
matlabTest=open(path+'matlabTest','w')
lines=svmTrainFile.readlines()
formatMatlabFile(lines,matlabTrain)
print('train done')
lines=svmTestFile.readlines()
formatMatlabFile(lines,matlabTest)
print('test done')
