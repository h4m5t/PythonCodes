#经典汉诺塔问题
def hanoi(n,a,b,c):

    if n==1:
        print(f"{a}->{c}")

    else:
        hanoi(n-1,a,c,b)
        print(f"{a}->{c}")
        hanoi(n-1,b,a,c)
hanoi(4,'x','y','z')

'''
9 3
1 1 A
1 0 A
1 -1 A
2 2 B
2 3 B
0 1 A
3 1 B
1 3 B
2 0 A
0 2 -3
-3 0 2
-3 1 1

'''

     