client=["harry","abhinav","vaibhav"]
data=["diet","work"]
def getdate():
    import datetime
    return datetime.datetime.now()
def menu():
    print("1.store data")
    print("2.retrive data")
    print("0.exit()")

def chooseClient():
    print("whose data you want to write")
    print("1.harry")
    print("2.abhinav")
    print("3.vaibhav")

def dietOrWork(c):
    print("About what you want to write of: ",client[c-1])
    print("1.diet")
    print("2.work")
   

def store(c,dw):
    if dw==1:
        with open (f"{client[c-1]}{data[dw-1]}.txt","a") as f:
            dietinfo=input("Enter the diet information...\n")
            f.write(str(getdate()))
            f.write("\n")
            f.write(dietinfo)
            f.write("\n")
    elif dw==2:
        with open (f"{client[c-1]}{data[dw-1]}.txt","a") as f:
            workinfo=input("Enter the workout information....\n")
            f.write(str(getdate()))
            f.write("\n")
            f.write(workinfo)
            f.write("\n")
    else:
        print("**Invalid operation..!!**")
def retrive(c,dw):
    if dw==1:
        with open (f"{client[c-1]}{data[dw-1]}.txt","r") as f:
            print(f.read())
    elif dw==2:
        with open (f"{client[c-1]}{data[dw-1]}.txt","r") as f:
            print(f.read())
    else:
        print("**Invalid operation..!!**")
a=True
while a!=0:    
    menu()
    a=int(input("Enter the operation that you want to perform\n"))
    if a==1:
        chooseClient()
        c=int(input("Enter the client number...\n"))
        dietOrWork(c)
        dw=int(input("Enter the operation that you want to do\n"))
        store(c,dw)
    elif a==2:
        chooseClient()
        c=int(input("Enter the client number...\n"))
        dietOrWork(c)
        dw=int(input("Enter the operation that you want to do\n"))
        retrive(c,dw)
