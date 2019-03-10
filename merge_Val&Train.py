fileNameList=["财经","彩票","房产","股票","家居","教育","科技","社会","时尚","时政","体育","星座","游戏","娱乐"]
strVal=""
strTrain=""
i=0
for fileName in fileNameList:
    fileValNamePath="extract/"+ fileName + "Val.txt"
    fileTrainNamePath="extract/"+ fileName + "Train.txt"
    f = open(fileValNamePath);  # 打开文件
    iter_f = iter(f);  # 创建迭代器
    for line in iter_f:  # 遍历文件，一行行遍历，读取文本
        i=i+1
        strVal = strVal + line
    print(i)

    f1 = open(fileTrainNamePath);  # 打开文件
    iter_f = iter(f1);  # 创建迭代器
    for line in iter_f:  # 遍历文件，一行行遍历，读取文本
        strTrain = strTrain + line

extractAllVal="extract/0extractAllVal.txt"
extractAllTrain="extract/0extractAllTrain.txt"
with open(extractAllVal,"w") as f:
    f.write(strVal)
with open(extractAllTrain,"w") as f:
    f.write(strTrain)
print("合并完毕！")

