import json,subprocess,datetime,sys

def say_hello(name,alive):
    line="Hello " + name + "!"
    if alive:
        line+=" WOW I'M A POKEMON FAN TOO!"
    else:
        line+=" ur not a fan of pokmon. u ded to me."
    return line

def do_addition(nb1,nb2):
    result=int(nb1)+int(nb2)
    return result