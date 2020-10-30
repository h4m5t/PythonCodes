x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x    # Python中可以用这样的方式来交换两个变量的值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("{}和{}的最大公约数是{}".format(x,y,factor))
        print("{}和{}的最小公倍数是{}".format(x,y,x*y//factor))
        # print(f'{x}和{y}的最大公约数是{factor}')
        # print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break