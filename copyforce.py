import os
import threading

#Running Website
def runWebsite():
    os.chdir("Website")
    os.system("py -m http.server")

#Running Api
def runApi():
    os.chdir("../Api")
    os.system("py -m app")
    
#Running Socket
def runSocket():
    os.chdir("../Socket")
    os.system("py -m CfSocket")

t1=threading.Thread(target=runWebsite)
t2=threading.Thread(target=runApi)
t3=threading.Thread(target=runSocket)
t1.start()
t2.start()
t3.start()