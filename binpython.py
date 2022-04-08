"""
 @header binpython.py
 @author xingyujie
 @abstract BINPython main file
"""
#BINPython By:XINGYUJIE AGPL-V3.0 LICENSE Release
#Please follow the LICENSE AGPL-V3

####################################
#configure

ver="0.15-stable"
#Don't change

libs_warning="1"  
#1 is ture 0 is false.
#Changing the value to 0 will close the prompt that the library does not exist

releases_ver="offical"
importlibs="os" #Don't use "import xxx"
#importlibs="<library>"
#Imported library name, please use "importlibs="<library name>" instead of "import <library name>"


####################################
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
#def
def help():
    print("[*] BINPython Help")
    print("""
-h     --help     View this help
-f     --file <filename>       Enter Python Filename and run
-s.    --server <port>    Start a simple web server that supports html and file transfer (http.server)
-v     --version  View BINPython Version
""")

#getopt
try:
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-s:-v',['help','file','server','version'])
except:
    print("Please check help:")
    help()
    print("The parameters you use do not exist or are not entered completely, please check help!  !  !  !  !")
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        help()
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
        exec("""

PORT = """ + server_port + """

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
""")
        sys.exit()
#main BINPython

print("BINPython " + ver + "-" + releases_ver + " (Python Version:" + platform.python_version() + ")By:XINGYUJIE https://github.com/xingyujie/binpython[Running on " + platform.platform() + " " + platform.version() + "]")
print('Type "about", "help", "copyright", "credits" or "license" for more information.')
try:
    while True:
        pycmd=input('>>> ')
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

