#BINPython By:XINGYUJIE AGPL-V3.0 LECENSE Release
#Please follow the LICENSE
import getopt
import sys
import platform
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
        print("BINPython By:XINGYUJIE[https://github.com/xingyujie] AGPL-3.0 LICENSE Release")
        print("Python " + platform.python_version())
        exit()
    if opt_name in ('-f','--file'):
        file = opt_value
        #print("[*] Filename is ",file)
        f = open(file,encoding = "utf-8")
        exec(f.read())
        #codeline=f.read()
        #codeline
        input("Please enter to continue")
        sys.exit()

print("BINPython 0.12 (Python Version:" + platform.python_version() + ")By:XINGYUJIE https://github.com/xingyujie[Running on " + platform.platform() + " " + platform.version() + "]")
print('Type "about", "help", "copyright", "credits" or "license" for more information.')

while True:
    x=input('>>> ')
    if x in globals().keys():
        print(globals()[x])
        continue
    elif x == 'about':
        print("BINPython By:XINGYUJIE[https://github.com/xingyujie] AGPL-3.0 LICENSE Release")
    elif x == 'help':
        print("Type help() for interactive help, or help(object) for help about object.")
    elif x == 'copyright':
        print("""
Copyright (c) 2001-2022 Python Software Foundation and BINPython xingyujie(https://github.com/xingyujie).
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
""")
    elif x == 'credits':
        print("""
Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
    """)
    elif x == 'license':
        print("Type license() to see the full license text")
    try:
        exec(x)
    except Exception as err:
        print(err)
