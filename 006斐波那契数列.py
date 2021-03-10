# a=1
# b=1
# print(a)
# print(b)
# for _ in range(30):
#     a=a+b
#     b=b+a

#     print(a)
#     print(b)
    
a, b = 1, 1
print(a, b, end=' ')
# 通过递推公式算出后面的18个数
for _ in range(30):
    a, b = b, a + b
    print(b, end=' ')