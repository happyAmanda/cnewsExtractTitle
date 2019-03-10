fileName="娱乐"
path = "extract/"+ fileName + ".txt" #文件夹目录
count = len(open(path,'rU').readlines())
print(count)
valNum = (int)(count/10)
print(valNum)
trainNum = count - valNum
print(trainNum)
fileValNamePath="extract/"+ fileName + "Val.txt"
fileTrainNamePath="extract/"+ fileName + "Train.txt"

fileAll = open(path)
#写入两个文件
i=0
for line in fileAll.readlines():
    i=i+1
    if(i == valNum):
        print("即将写入train文件,现在是：",i)
    if(i <= valNum):
        with open(fileValNamePath,"a") as one:
            one.write(line)
    else:
        with open(fileTrainNamePath,"a") as two:
            two.write(line)

print("写入完毕！")




