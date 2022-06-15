import os

x=[]
y=[]
z=[]
def app():
    du = os.popen("df -k").readlines()
    for line in du:
            # print(i)
        line = line.replace('"', '').strip()
        list_1 = line.split()
            # print(type(list_1))
        x.append(list_1[1])
        y.append(list_1[2])
        z.append(list_1[3])
    # print(x)
    # print(y)
    # print(z)
    for i in x[1:]:
        a=int(i)
        # print(type(a))
        decimal_places=2
        for unit in ['Byte','KB','MB','GB','TB','PB']:
            if a < 1024.0:
                break
            a /= 1024.0
        print(f"{a:.{decimal_places}f}{unit}")
    
   
app()