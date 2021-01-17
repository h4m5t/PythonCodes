'''
预测性别比例
假设每个家庭生孩子，直到生出男孩，便停止。
试问，如果每个家庭都这样，最终男女比列是多少？
'''
import random

def sex():
    #1表示男，0表示女
    return random.randint(0,1)

def birth():
    #算每个家庭的女孩个数
    girl=0
    while True:
        thesex=0
        thesex=sex()
        if thesex==1:
            break
        else:
            girl+=1
    return girl

if __name__ == "__main__":
    #假设有10000个家庭
    n=10000
    total_girl=0
    for i in range(n):
        temp=birth()
        total_girl=total_girl+temp
    print(f'生了{n}个男孩{total_girl}个女孩')


    

