import random
import os
import subprocess

def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    new_ = ""
    for i in range(1,5):
        new_+=get_rand()+get_rand()+":"
    new_+=get_rand()+get_rand()
    return new_

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))
subprocess.call(["sudo","ifconfig","eth0","down"])
subprocess.call(["sudo","service","network-manager","stop"])
new_m = new_mac()
subprocess.call(["sudo","ifconfig","eth0","hw","ether","00:%s"%new_m])
subprocess.call(["sudo","service","network-manager","start"])
subprocess.call(["sudo","rfkill","unblock","all"])
subprocess.call(["sudo","ifconfig","eth0","up"])
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))
