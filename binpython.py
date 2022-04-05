#BINPython By:XINGYUJIE AGPL-V3.0 LECENSE Release
#Please follow the LICENSE

#base import
import getopt
import sys
import platform
#gui import
try:
    import tkinter
    import turtle
#warning for gui
except:
    print("Warning: Some GUI (graphical) libraries for BINPython do not exist, such as tkinter and turtle.  Because they are not built when they are built.  If you need to fix this warning, please complete the support libraries imported in the source code at build time (use pip or build it yourself), if your system does not support these libraries, you can remove or change this hint in the source code and rebuild")
    print("")

#import math
try:
    import fractions
    import cmath
except:
    print("Warning: Some math or computation libraries for BINPython do not exist, such as fractions and cmath.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
    print("")
#rlcompleter
#import for normal
try:
    #str
    import rlcompleter
    import array
except:
    print("Warning: Some libraries for functions, data types, etc. for BINPython do not exist, such as rlcomplter and array.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
    print("")
try:
     import filecmp
     import tempfile
except:
     print("Warning: Some file manipulation libraries for BINPython do not exist, such as filecmp and tempfile.  Because they weren't built when they were built.  If you need to fix this warning, please complete the support libraries imported in the source code when building (use pip or build it yourself), if your system does not support these libraries, you can remove or change this prompt in the source code and rebuild")
     print("")
#getopt
opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','file=','version'])
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        print("[*] Help info")
        print("""
-h     --help     View this help
-f     --file=     Enter Python Filename and run
-v     --version  View BINPython Version
""")
        sys.exit()
    if opt_name in ('-v','--version'):
        print("BINPython By:XINGYUJIE[https://github.com/xingyujie/binpython] AGPL-3.0 LICENSE Release")
        print("Python " + platform.python_version())
        exit()
    if opt_name in ('-f','--file'):
        file = opt_value
        f = open(file,encoding = "utf-8")
        exec(f.read())
        input("Please enter to continue")
        sys.exit()
#main BINPython

print("BINPython 0.14 (Python Version:" + platform.python_version() + ")By:XINGYUJIE https://github.com/xingyujie/binpython[Running on " + platform.platform() + " " + platform.version() + "]")
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

