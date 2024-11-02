#!/bin/python3

import os, subprocess, shutil, sys

tsize=os.get_terminal_size()[0]
path=subprocess.getoutput('echo $PATH | cut -d ":" -f1')

check_file = lambda directory_name: os.path.isfile(directory_name)

def clear(): os.system("clear")

def main_logo():
    clear()
    print("\x1b[1;96m┏"+"─"*(tsize-2)+"┓\x1b[00m")
    print("\x1b[1;96m│"+" "*(tsize-2)+"│")
    print("\x1b[1;96m│\x1b[38;5;82m"+"██████╗  █████╗ ██╗██████╗ ██╗  ██╗".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│\x1b[38;5;83m"+"██╔══██╗██╔══██╗██║██╔══██╗╚██╗██╔╝".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│\x1b[38;5;84m"+"██████╔╝███████║██║██║  ██║ ╚███╔╝ ".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│\x1b[38;5;85m"+"██╔═══╝ ██╔══██║██║██║  ██║ ██╔██╗ ".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│\x1b[38;5;86m"+"██║     ██║  ██║██║██████╔╝██╔╝ ██╗".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│\x1b[38;5;87m"+"╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝".center(tsize-2)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│"+" "*(tsize-2)+"│\x1b[00m")
    print("\x1b[1;96m┣"+"─"*(tsize-2)+"┫\x1b[00m")
    print("\x1b[1;96m│"+"\033[1;32m[\033[1;91m❃\033[1;32m] \033[1;97mDEVELOPER    \x1b[38;5;45m——\x1b[38;5;121m-\x1b[38;5;45m——\x1b[38;5;40m      JAME-404    ".center(tsize+67)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│"+"\033[1;32m[\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM     \x1b[38;5;45m——\x1b[38;5;121m-\x1b[38;5;45m——\x1b[38;5;40m  t.me/JAMES_2007 ".center(tsize+67)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m│"+"\033[1;32m[\033[1;91m❃\033[1;32m] \033[1;97mTG CHANNEL   \x1b[38;5;45m——\x1b[38;5;121m-\x1b[38;5;45m——\x1b[38;5;40m  t.me/JAME_EMPIRE".center(tsize+67)+"\x1b[1;96m│\x1b[00m")
    print("\x1b[1;96m┗"+"─"*(tsize-2)+"┛\x1b[00m")

def get_python_module_path():
    for dir in sys.path:
        if "site-packages" in dir:
            for pkg in os.listdir(dir+"/"):
                if "requests" in pkg:
                    break
    return dir+"/"+pkg+"/"

module_path = get_python_module_path()
module_path = module_path.split("site-packages")[0]

def uninstall():
    global module_path, path
    if check_file(path+"/paidx"):
        os.system(f"rm -rf {path}/paidx")
    if check_file(module_path+"paidx.cpython-312.so"):
        os.system(f"rm -rf {module_path}paidx.cpython-312.so")

def touch_paidx():
    content='#!/bin/python3\nimport paidx'
    open("paidx","w").write(content)

def install():
    touch_paidx()
    global module_path, path
    if check_file("paidx"):
        shutil.move("paidx", path+"/")
        os.chmod(path+"/paidx", 0o777)
    if check_file("paidx.cpython-312.so"):
        shutil.move("paidx.cpython-312.so", module_path)

def main():
    main_logo()
    print("\x1b[1;97m[1] Install Command")
    print("[2] Uninstall Command")
    optz=input("Enter option (1/2) : ").lower()
    if optz in ("1", "one", "i", "install", "install command"):
        install()
        print('\x1b[1;92mRun type "\x1b[1;96mpaidx\x1b[1;92m"')
    elif optz in ("2", "two", "u", "uninstall", "uninstall command"):
        uninstall()

if(__name__=="__main__"):main()
