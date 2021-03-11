#整数转IP地址
n=int(input())




s=bin(n)[2:].zfill(32)

t=[0,0,0,0]
t[0]=s[:8]
t[1]=s[8:16]
t[2]=s[16:24]
t[3]=s[24:32]


def function(num):
    t=int(num,2)
    s=str(t)
    return s

res=""
for i in range(4):

    t[i]=function(t[i])
result=".".join(t)

print(result)