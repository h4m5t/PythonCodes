import hashlib

tmp=hashlib.md5()

def generate_md5(str:str):
    tmp=hashlib.md5()
    tmp.update(str.encode(encoding="utf-8"))
    return tmp.hexdigest()
    

for i in range(10000000):
    t=str(i)
    res=generate_md5(t)
    if res.startswith("66666"):
        print(i)
        print(res)




