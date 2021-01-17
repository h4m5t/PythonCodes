#制作一个密码生成器
#规则如下：
'''
密码长度不能小于6
密码里可以包含英文字母，数字，符号
至少包含一个大写字母
至少包含一个特殊符号
'''
import random
#定义函数随机生成1~3个大写字母
def get_upper():
    count=random.randint(1,3)
    return random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=count)

#随机生成符号
def get_special_char():
    count=random.randint(1,3)
    return random.choices('！@#￥%&*-=+~',k=count)

def get_lower(count):
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return random.choices(string, k=count)

def generate_password(length):
    if length<6:
        length=6
    
    lst=[]
    upper_lst=get_upper()
    special_char=get_special_char()
    lst.extend(upper_lst)
    lst.extend(special_char)
    surplus_count = length - len(lst)
    lower_lst = get_lower(surplus_count)

    lst.extend(lower_lst)

    #打乱顺序
    random.shuffle(lst)
    return ''.join(lst)

if __name__ == "__main__":
    #进行测试
    for i in range(10):
        random_length=random.randint(4,16)
        print(generate_password(random_length))



    
