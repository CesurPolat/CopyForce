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

t1=threading.Thread(target=runWebsite)
t2=threading.Thread(target=runApi)
t1.start()
t2.start()