import os

#Running Website
os.chdir("Website")
os.system("py -m http.server")

#Running Api
os.chdir("../Api")
os.system("py -m app")