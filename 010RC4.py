import base64
import os
import struct
import time
#密钥函数
def get_key():
    print("输入你的秘钥：")
    key = input()
    return key

#用key初始化S盒
def init_box(key):
    s_box = list(range(256)) 
    #print(s_box)
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]   
    return s_box

#D为字节，S为空表
def rc4_Decrypt(S, D): 
    i = j = 0
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    t = (S[i] + S[j]) % 256

    k = (ord(D) ^ S[t])    
    k=struct.pack('B',k)
    return k

if __name__ == '__main__':
    print("请选择加密或者解密")
    print("1. Encrypt")
    print("2. Decode")
    mode = input()
    if mode == '1':
        filepath=input("请输入你要加密的文件路径：")
        #增加测速功能
        f=open(filepath,mode='rb')
             
        key = get_key()
        box = init_box(key)
        size = os.path.getsize(filepath) #获得文件大小
        msize=size/(1024*1024)
        print("文件大小：%0.5f"%msize+' MB')
        tim=filepath[-4:]
        outputfilepath='C:\\Users\\loeoe\\Desktop\\output'+tim+'.RC4'
        fin=open(outputfilepath,mode='ab')
        start = time.perf_counter()  
        for i in range(size):
            data = f.read(1) #每次输出一个字节           
            #加密后的字节为
            #new_data=ex_encrypt(data,box,mode)
            fin.write(rc4_Decrypt(box,data))
        
        end = time.perf_counter()
        fin.close()
        f.close()
        
        alltime=end-start
        print("加密耗时: %0.5s"%alltime+' s')
        v=msize/alltime
        print("加密速率：%0.5s"%v+' MB/s')
        time.sleep(10)

    elif mode == '2':       
        key = get_key()
        box = init_box(key)   
        filepath=input("请输入你要解密的文件路径：")      
        f=open(filepath,mode='rb')    
        start = time.perf_counter()
        size = os.path.getsize(filepath) #获得文件大小
        msize=size/(1024*1024)
        print("文件大小：%0.5f"%msize+' MB')
        tim=filepath[:-4]       
        fin=open(tim,mode='ab')

        start = time.perf_counter()
        for i in range(size):
            data = f.read(1) #每次输出一个字节           
            #加密后的字节为
            #new_data=ex_encrypt(data,box,mode)
            fin.write(rc4_Decrypt(box,data))

        end = time.perf_counter()
        fin.close()
        f.close()
              
        alltime=end-start
        print("解密耗时: %0.5s"%alltime+' s')
        v=msize/alltime
        print("解密速率：%0.5s"%v+' MB/s')
        time.sleep(10)

    else:
        print("输入有误！")
