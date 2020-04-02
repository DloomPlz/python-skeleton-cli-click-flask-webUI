import json,subprocess,datetime,sys

def say_hello(name,alive):
    line="Hello " + name + "!"
    if alive:
        line+=" We are glad you are alive!"
    else:
        line+=" sad U ded."
    return line

def do_addition(nb1,nb2):
    result=int(nb1)+int(nb2)
    return result