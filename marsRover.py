input("")
a = []
def cont(adic):
    dicrot=""
    if (adic%4==0):
        dicrot="N"
    elif(adic%4==1):
        dicrot = "E"
    elif(adic%4==2):
        dicrot = "S"
    else:
        dicrot = "W"
    return dicrot
for j in range (0,2):
    x = 0
    y = 0
    direc = 0
    b = []
    a.append(input(""))
    if (a[j].split(" ")[2].lower() =="n"):
        direc=0
    elif(a[j].split(" ")[2].lower() =="e"):
        direc = 1
    b=input()
    for i in range(0,len(b)):
        if(b[i].lower()=="m"):
            if(direc%4==0):
                y+=1
            elif(direc%4==1):
                x+=1
            elif(direc%4==2):
                y-=1
            elif(direc%4==3):
                x-=1
        elif(b[i].lower() == "l"):
            direc-=1
        elif(b[i].lower() == "r"):
            direc+=1
        else:
            print("error")

    print(int(a[j].split(" ")[0])+x ," ", int(a[j].split(" ")[1])+y, cont(direc))



