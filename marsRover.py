input("")
a = []
for j in range (0,2):
    x = 0
    y = 0
    direc = 0
    b = []
    a.append(input(""))
    if (a[j].split(" ")[2]== "N" or a[j].split(" ")[2] =="n"):
        direc=0
    elif(a[j].split(" ")[2]== "E" or a[j].split(" ")[2] =="e"):
        direc = 1
    b=input()
    for i in range(0,len(b)):
        if(b[i]=="M"):
            if(direc%4==0):
                y+=1
            elif(direc%4==1):
                x+=1
            elif(direc%4==2):
                y-=1
            elif(direc%4==3):
                x-=1
        elif(b[i] == "L"):
            direc-=1
        elif(b[i] == "R"):
            direc+=1
        else:
            print("error")

    print(int(a[j].split(" ")[0])+x ," ", int(a[j].split(" ")[1])+y, "N" if direc%4==0 else "E" )



