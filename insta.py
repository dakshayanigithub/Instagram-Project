class insta:
    def __init__(self,company) -> None:
        self.company=company
        self.d={}
    def addinstaaccount(self,object):
        self.d[object.username]=[]
        self.d[object.username].append(object.username)
        self.d[object.username].append(object.password)
        self.d[object.username].append(object.following)
        self.d[object.username].append(object.followers)
        self.d[object.username].append(object.post)
        self.d[object.username].append(object.profile)
        self.d[object.username].append(object.request)
    def createpost(self,username):
         text=input("write a post")
         self.d[username][4][0]+=1
         self.d[username][4][1].append(text)
         print("successfully posted")
    def sendrequest(self,username,other):
        self.d[other][6].append(username)
    def acceptrequest(self,username):
        print(self.d[username][6])
        name=input("enter name")
        self.d[username][6].remove(name)
        self.d[username][3][0]+=1
        self.d[username][3][1].append(name)
        self.d[name][2][0]+=1
        self.d[name][2][1].append(username)
    def showprofile(self,username):
        print("following:-",self.d[username][2])
        print("followers:-",self.d[username][3])
        print("post:-",self.d[username][4])
        print("profile:-",self.d[username][5])
        print("request:-",self.d[username][6])
        
        
        
        
        
    def sendmoney(self,username,reciever):
       amount=int(input("enter the amount"))
       while amount>self.d[username][2]:
           print("Low balance")
           amount=int(input("enter the amount"))
       else:
             self.d[username][2]>=amount
             self.d[username][2]-=amount
             self.d[reciever][2]+=amount
             value=("i haven sent")+str(amount)+"rs to"+ reciever + " curr balance is "+ str(self.d[username][2])
             self.d[username][3].append(value)
             value=("i haven recieved")+str(amount)+"from"+ username + " curr balance is "+ str(self.d[reciever][2])
             self.d[reciever][3].append(value)
             print("Transaction successfull")
             
             
class Account:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.following=[0,[]]
        self.followers=[0,[]]
        self.post=[0,[]]
        self.profile=[]
        self.request=[]
        
        
        
        
        
        
        
#homepage
ins=insta("Instagram")
option=0
while option!=3:
    print("")
    print("1.Create an account")
    print("2.Login in")
    print("3.Exit")
    
    print("")
    i=int(input("choose an option:"))
    if i==1:
        
        print("welcome to Instagram:")
        username=input("Enter your username:")
        password=input("Set your password")
        if username in ins.d:
            print("Account Already exists")
            continue
        username=Account(username,password)
        ins.addinstaaccount(username)
        print(ins.d)
        print("Congrats, your account has been created ")
    elif i==2:
        print()
        print("")
        u=input("Enter your username: " )
        p=input("Enter your password: ")
        if u not in ins.d:
                print("Account does not exits ")
                
                continue
        else:
            i=1
            while i<4:
                if p==ins.d[u][1]:
                      print()
                      print("")
                      q=0
                      while( q<6):
                            print("welcome ,",ins.d[u][0])
                            print("1.Create post")
                            print("2.send request")
                            print("3.Accept request")
                            print("4.Show Profile")
                            print("5.log out")
                            print()
                            i=int(input("Choose your option"))
                            if i==1:
                                ins.createpost(u)
                            elif i==2:
                                m=input("Enter the username")

                                while m not in ins.d:
                                    print("Enter Valid username")
                                    m=input("Re enter")
                                else:
                                    ins.sendrequest(u,m)
                                
                                    
                            elif i==3:
                                ins.acceptrequest(u)
                            elif i==4:
                                ins.showprofile(u)
                            elif i==5:
                                break
                            else:
                                print("invalid option")
                            print("")
                      break
                else:
                    print("wrong password",3-i,"attempt left")
                    p=input("Enter your password: ")
                i+=1         
    elif i==3:
        exit()
        
    else:
        print("Invalid option")
