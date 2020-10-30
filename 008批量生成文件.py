#实现批量生成文件
list1=range(10)
for i in range(10):
    filepath=r"Learn2\\"+'0'+str(i)+'.py'

    print(filepath)

    f=open(filepath,mode='w',encoding='utf-8')
    #f.write('123我爱你')
    f.close()