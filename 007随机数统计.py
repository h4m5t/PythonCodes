
import random
from tqdm import tqdm
#随机数概率测试
#用一个列表来存储出现的次数
list1=[0]*10

#生成1~10的一百万个随机数
for i in tqdm(range(1000000)):
    a=random.randint(1,10)
    list1[a-1]+=1
    #print(a,end=' ')
print("\n")
for i in range(0,10):
    print('%2d：%8d次, 比率：%f'%(i+1,list1[i],list1[i]/1000000))






