import zipfile
klist = ["111","12345","112345","nwi1ii1o","12345","123457","123456","0000000","hi998899","hg8666666"]

zfile = zipfile.ZipFile("succ.zip")
n=0 
def vzip(pwd):
    try:
        zfile.extractall(pwd=pwd)
        zfile.close()
        return pwd
    except Exception as e:
        print(e)
        return 0


for k in klist:
    kp = bytes(k,"utf-8")
    if n == 0:
        print(k)
        n = vzip(kp)
        
    else:
        break
print("The passwords is:",n)




