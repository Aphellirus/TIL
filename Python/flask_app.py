import subprocess
import sys

#use this install() function to pip-install modules
def install(package):

    subprocess.run([
        sys.executable, "-m", "pip", "-q", "install", package
    ])
install("flask")


# import  flask from flask class Flask
from flask import Flask 
from flask import Flask

# App Run Module 
# Root App 
Root = Flask(__name__)

# Just Test Server 
def server() :
    return "Hello World"

server()

if __name__ == "main" :
    print("Thank You")

# App Run 
Root.run()
