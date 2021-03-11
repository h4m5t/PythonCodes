nums=list(map(int,input().split(".")))

#输入整数，转换为二进制字符串
def convert(num):
    t=bin(num)[2:].zfill(8)
    return t

res=""
for i in range(4):
    res=res+convert(nums[i])

res=int(res,2)
print(res)

    

