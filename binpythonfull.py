"""
 @header binpython.py
 @author xingyujie https://github.com/xingyujie
 @abstract BINPython main file
"""
#BINPython By:XINGYUJIE AGPL-V3.0 LICENSE Release
#Please follow the LICENSE AGPL-V3
#full version
####################################
#build configure

ver="0.23-releases-full"

libs_warning="1"
#1 is ture 0 is false.
#Changing the value to 0 will close the prompt that the library does not exist


buildversion = "plus" #plus version and standard version

releases_ver="offical" + buildversion + "-building"
importlibs="os" #Don't use "import xxx" 
#Imported library name, please use "importlibs="<library name>" instead of "import <library name>"
#Please note: The "importlibs" function does not support loading functions (such as from xxxx import xxxx, if necessary, please write it in the following location. However, please note that this operation may have the risk of error reporting, please report issues or solve it yourself
#xxxxxxxxxxxxxx

#from xxxx import xxxx
#xxxxxxxxxxxxxx
####################################
#BINPython function and variable START
def binpython_ver():
    print(ver)

def binpython_buildversion():
    print(buildversion)

def binpython_libs_warning():
    print(libs_warning)

def binpython_releases_ver():
    print(releases_ver)

def binpython_build_importlibs():
    print(importlibs)
import platform
sys = platform.system()

if sys == "Windows":
    def setwindowtitle(titlename):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(titlename)
def binpythonallconf():
    print("ver: " + ver + " buildversion: " + buildversion + " libs_warning settings:" + libs_warning + " releases full version: " + releases_ver + " custom library that has been build: " + importlibs)
if sys == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("BINPython " + ver)
def self_import(name):
    __import__(name)
try:
    self_import(importlibs)
except ImportError:
    if libs_warning == "1":
        print("Warning: Custom import library %s does not exist, please check the source code library configuration and rebuild" % importlibs)
        print("")
try:
#base import
    import getopt
    import sys
    import platform
    import os
#fix for exit()
    from sys import exit
#import for http_server
    import http.server
    import socketserver
#except ImportError:
except ImportError:
    print("Unable to use any library, the program does not work properly, please rebuild")
#gui import
try:
    import tkinter
    import tkinter as tk
    from tkinter import *
    import turtle
#warning for gui
except ImportError:
    if libs_warning == "1":
        print("Warning: Some GUI (graphical) libraries for BINPython do not exist, such as tkinter and turtle.  Because they are not built when they are built.  If you need to fix this warning, please complete the support libraries imported in the source code at build time (use pip or build it yourself), if your system does not support these libraries, you can remove or change this hint in the source code and rebuild")
        print("")

#import math
try:
    import fractions
    import cmath
except ImportError:
    if libs_warning == "1":
        print("Warning: Some math or computation libraries for BINPython do not exist, such as fractions and cmath.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
        print("")
#rlcompleter
#import for normal
try:
    #str
    import rlcompleter
    import array
except ImportError:
    if libs_warning == "1":
        print("Warning: Some libraries for functions, data types, etc. for BINPython do not exist, such as rlcomplter and array.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
        print("")
try:
     import filecmp
     import tempfile
except ImportError:
    if libs_warning == "1":
        print("Warning: Some file manipulation libraries for BINPython do not exist, such as filecmp and tempfile.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
        print("")
#main BINPython

def binpython_shell():
    print("BINPython " + ver + "-" + releases_ver + " (Python Version:" + platform.python_version() + ")By:XINGYUJIE https://github.com/xingyujie/binpython[Running on " + platform.platform() + " " + platform.version() + "]")
    print('Type "about", "help", "copyright", "credits" or "license" for more information.')
    try:
        while True:
            pycmd=input(">>> ")
            if pycmd in globals().keys():
                print(globals()[pycmd])
                continue
            elif pycmd == 'about':
                print("BINPython By:XINGYUJIE[https://github.com/xingyujie] AGPL-3.0 LICENSE Release")
            elif pycmd == 'help':
                print("Type help() for interactive help, or help(object) for help about object.")
            elif pycmd == 'copyright':
                print("""
Copyright (c) 2001-2022 Python Software Foundation and BINPython xingyujie(https://github.com/xingyujie/binpython).
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
""")
            elif pycmd == 'credits':
                print("""
Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
    """)
            elif pycmd == 'license':
                print("Type license() to see the full license text")
            try:
                exec(pycmd)
            except Exception as err:
                print(err)
    except KeyboardInterrupt:
        print("EXIT!")
        sys.exit()


#def
helpinfobase = """
Usage: binpython [OPTIONS]

Options:

-h            --help               View this help
-f <filename> --file=<filename>    Enter Python Filename and run (*.py)
-s <port>     --server=<port>      Start a simple web server that supports html and file transfer (http.server)
-v            --version            View BINPython Version
-g            --gui                View GUI About and build info
-i            --idle               Open BINPython IDLE Code Editor
"""
helpinfoplus = """
-p            --plus               Open BINPython IDE Plus Code Editor(beta) with http web server
-e            --example            Run various code examples through BINPython
"""
about = "BINPython " + ver + "-" + releases_ver + " By:XINGYUJIE[https://github.com/xingyujie/binpython] AGPL-3.0 LICENSE Release"
#getopt
try:
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-s:-g-i-p-v',['help','file=','server=','gui','idle','plus','version'])
except:
    print("Please check help:")
    help()
    print("The parameters you use do not exist or are not entered completely, please check help!  !  !  !  !")
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        
        print(helpinfobase)
        print("Standard options")
        if buildversion == "plus":
            print("Additional options for the plus version")
            print(helpinfoplus)
        sys.exit()
    if opt_name in ('-v','--version'):
        print("BINPython " + ver + "-" + releases_ver + " By:XINGYUJIE[https://github.com/xingyujie/binpython] AGPL-3.0 LICENSE Release")
        print("Python " + platform.python_version())
        exit()
    if opt_name in ('-f','--file'):
        file = opt_value
        f = open(file,encoding = "utf-8")
        exec(f.read())
        input("Please enter to continue")
        sys.exit()
    if opt_name in ('-s','--server'):
        server_port = opt_value
        print("""
PORT = """ + server_port + """

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
""")
    if opt_name in ('-g','--gui'):
        from tkinter import *
        root = Tk()
        root.title("Welcome to BINPython")
        root.geometry('600x300')
        text =Text(root, width=35, heigh=15)
        text.pack()
        text.insert("insert", "BINPython" + about)
        print(text.get("1.3", "1.end"))
        ####
        text=Label(root,text="Welcome to BINPython" + ver,bg="yellow",fg="red",font=('Times', 20, 'bold italic'))
        text.pack()
        button=Button(root,text="EXIT",command=root.quit)
        button.pack(side="bottom")
        root.mainloop()
        sys.exit()
    def show():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("<<<<<<<<<<START>>>>>>>>>>")
        exec(e1.get(1.0, END))
    if opt_name in ('-i','--idle'):
        import tkinter as tk
        from tkinter import *
        import os
        master = tk.Tk()
        master.title("BINPython IDLE")
        
 
        tk.Label(master, text="Type Code", height=5).grid(row=0)
 
        e1 = Text(master,
            width=150,
            height=40,)
        
        e1.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(master, text="Run", width=10, command=show).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Button(master, text="EXIT", width=10, command=master.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)
        master.mainloop()
    if opt_name in ('-p','--plus'):
        serverport = input("Please enter server port(like 8080): ")
        import pywebio.input
        from pywebio.input import *
        from pywebio.output import *
        from pywebio import *
        from pywebio.session import *
        import sys
        import subprocess
        import os
        print("______________________________________")
        print("BINPython WEB IDE STARTED")
        #IDE Plus main
        def main():
            set_env(title="BINPython IDE Plus", auto_scroll_bottom=True)
            put_html("<h1>BINPython IDE Plus</h1>")
            put_text('Welcome to BINPython IDE Plus, Please type code',
                    sep=' '
                )
            toast("BINPython IDE Plus is a beta version. May be removed or changed in the future")
            put_text('_______________________',
                sep=' '
            )
            res = textarea('BINPython IDE Plus', rows=45, code={
            'mode': "python",
            'theme': 'darcula'
            })
            exec(res)
            toast("Run finished!")
            put_success("Finished, Please see BINPython Window or Terminal")
            put_text("Here is the code you wrote")
            put_code(res, language='python')
            savecodefilename = pywebio.input.input('Do you want to save the code you wrote to a file? Enter a filename and save it')
            f = open(savecodefilename, 'wb+')
            f.write(res.encode("utf-8"))
            toast("Successfully saved")
            put_success("The save is successful, and the code is saved to binpython file path" + " \nThe file name is " + '"' + savecodefilename + '"')
        if __name__ == '__main__':
            start_server(main, debug=True, host='0.0.0.0', port= serverport)
            pywebio.session.hold()
       
#go main shell
binpython_shell()