def trans_to_list(num):
    list1=[]
    for i in range(4):
        x=num%10
        list1.append(x)
        num=int(num/10)
    list1.reverse()
    return list1

def trans_to_num(list):
    num=0
    for i in range(4):
        num=num*10+list[i]
    return num

#数字黑洞
def num_back_hole(num):
    print(num,end="")
    while True:
        list0=trans_to_list(num)
        a=sorted(list0)
        Min=trans_to_num(a)
        b=sorted(list0,reverse=True)
        Max=trans_to_num(b)

        #print(Min,Max)
        num=Max-Min
        print("->"+str(num),end="")
        if num==6174:
            break

num_back_hole(6767)

