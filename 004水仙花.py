#求水仙花数
#例如：1^3+3^3+5^3=153

#我的方法
'''
for i in range(100,1000):
    #求出百位十位个位x,y,z
    x=i//100
    y=(i-x*100)//10
    z=(i-(x*100)-(y*10))

    #print("{}的百位是{}十位{}个位{}".format(i,x,y,z))
    result=x**3+y**3+z**3
    if result==i:
        print(i)
'''
#大佬的方法
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


