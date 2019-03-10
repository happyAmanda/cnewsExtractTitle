import os
fileName="娱乐"
path = "../THUCNews/"+ fileName #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
str = ""
num=0
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          num=num+1
          print("第",num,"次打开文件")
          f = open(path+"/"+file); #打开文件
          iter_f = iter(f); #创建迭代器
          i=0
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              if i == 0:
                  LinePack = fileName + "	" + line
                  str = str + LinePack
              i = i + 1
extractFile="extract/" + fileName +".txt"
with open(extractFile,"w") as f:
    f.write(str)
print("读取完毕！")
print("总条目为：",num) #打印结果
