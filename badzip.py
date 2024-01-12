import zipfile
k = 0

zfile = zipfile.ZipFile("succ.zip")
n=0 
def vzip(pwd):
    try:
        zfile.extractall(pwd=pwd)
        zfile.close()
        n = 1
    except Exception as e:
        print(e)
        pass

while True:
    kp = bytes(k)
    if n == 0:
        print(k)
        vzip(kp)
        k += 1

    else:
        break




