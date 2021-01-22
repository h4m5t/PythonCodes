#定义一个函数，求一个数字的每一位
def num(n):
    length=len(str(n))
    for i in range(0,length):
        t=10**i
        number=(n//t)%10
        print(number)
#test      
num(123456789)


