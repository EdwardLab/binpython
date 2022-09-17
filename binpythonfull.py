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

ver = "0.34-build-full"

libs_warning = "1"
#1 is ture 0 is false.
#Changing the value to 0 will close the prompt that the library does not exist

buildversion = "plus" #plus version and standard version

releases_ver = "offical" + buildversion + "-building"
importlibs = "os" #Don't use "import xxx" 
cloudrunver = "1.01"
#Imported library name, please use "importlibs="<library name>" instead of "import <library name>"
#Please note: The "importlibs" function does not support loading functions (such as from xxxx import xxxx, if necessary, please write it in the following location. However, please note that this operation may have the risk of error reporting, please report issues or solve it yourself
#xxxxxxxxxxxxxx

#from xxxx import xxxx
#xxxxxxxxxxxxxx
####################################
#BINPython function and variable START
class binpythoninfo:
    def ver():
        print(ver)

    def buildversion():
        print(buildversion)

    def libs_warning():
        print(libs_warning)

    def releases_ver():
        print(releases_ver)

    def build_importlibs():
        print(importlibs)
#get system info(windows or linux ...)
import platform
sys = platform.system()
#if system is windows, then enable setwindowtitle() function
if sys == "Windows":
    class binpythonwin:
        def setwindowtitle(titlename):
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(titlename)
#print binpython all configure function
def binpythonallconf():
    print("ver: " + ver + " buildversion: " + buildversion + " libs_warning settings:" + libs_warning + " releases full version: " + releases_ver + " custom library that has been build: " + importlibs)
#if system is windows, show default window title
if sys == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("BINPython " + ver)
#binpython self import function
def self_import(name):
    __import__(name)
try:
    self_import(importlibs)
#get libswarning
except ImportError:
    if libs_warning == "1":
        print("Warning: Custom import library %s does not exist, please check the source code library configuration and rebuild" % importlibs)
        print("")
#run python files option(-f)
def optreadfile():
    import sys
    getfile = sys.argv[1]
    getfilecode = open(getfile,encoding = "utf-8")
    exec(getfilecode.read())
    input("Run finished. Enter to Shell.")
    sys.exit(0)
class cloudrun:
    def get(pkgname):
        try:
            cloudrunenv = True
            getcoderes = urllib.request.urlopen(f"https://raw.githubusercontent.com/xingyujie/cloudrun-repository/main/{pkgname}.py")
        except(Exception, BaseException) as error:
            print("There is no network connection or the repository does not exist for this script")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write(str(error))
        try:
            exec(str(getcoderes.read().decode('utf-8')))
            getcoderes.close()
        except(Exception, BaseException) as error:
            print("run failed")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write(str(error))
    def load(url):
        try:
            cloudrunenv = True
            getcoderes = urllib.request.urlopen(url)
        except(Exception, BaseException) as error:
            print("There is no network connection or the repository does not exist for this script")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write(str(error))
        try:
            exec(getcoderes.read().decode('utf-8'))
            getcoderes.close()
        except(Exception, BaseException) as error:
            print("run failed")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write(str(error))
try:
#base import
    import getopt
    import sys
    import platform
    import os
    import timeit
    import pdb
    import random
    import webbrowser
    import urllib.request
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
    def importpygame():
        import pygame
        import pygame.locals
        import pyglet
    null = importpygame
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
#import for normal
try:
    #str
    import rlcompleter
    import array
    import xlrd
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
def binpython_welcome_text():
    print("BINPython " + ver + "-" + releases_ver + " (Python Version:" + platform.python_version() + ")By:XINGYUJIE https://github.com/xingyujie/binpython[Running on " + platform.platform() + " " + platform.version() + "]")
    print('Type "about", "help", "copyright", "credits" or "license" for more information.')
def binpython_shell():
    while True:
        try:
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
Copyright (c) 2001-2022 Python Software Foundation.
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
            else:
                exec(pycmd)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            sys.exit()
        except Exception as err:
            print(err)
try:
    optreadfile()
except:
    pass





#def
#helpinfo base
helpinfobase = """
Usage: binpython [OPTIONS]

Options:
<filename>                         Enter Python Filename and run (*.py)
-f            --file               Enter Python Filename and run (*.py), But this options is no Run finished prompt
-h            --help               View this help
-s <port>     --server=<port>      Start a simple web server that supports html and file transfer (http.server)
-v            --version            View BINPython Version
-g            --gui                View GUI About and build info
-i            --idle               Open BINPython IDLE Code Editor
"""
#helpinfo plus
helpinfoplus = """
-p <port>     --plus=<port>        Open BINPython IDE Plus Code Editor(beta) with http web server
-e            --example            Run various code examples through BINPython
-c            --cloudrun           Run Python scripts in the cloud via CloudRun (into CloudRun CLI)
"""
#base + plus, print full help
def outputfullhelp():
    try:
        f = open("binpython_config/help.txt",encoding = "utf-8")
        print(f.read())
    except:
        print(helpinfobase)
        if buildversion == "plus":
            print("Additional options for the plus version")
            print(helpinfoplus)
#set about info
about = "BINPython " + ver + "-" + releases_ver + " By:XINGYUJIE[https://github.com/xingyujie/binpython] AGPL-3.0 LICENSE Release"
#getopt
try:
#set options
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-s:-g-i-p:-e-c-v',['help','file=','server=','gui','idle','plus','example','cloudrun','version'])
#set getopt error prompt
except getopt.GetoptError as err:
    print("Please check help:")
    print("The parameters you use do not exist or are not entered completely, please check help!!!!")
#then show full help(outputfullhelp())
    outputfullhelp()
    sys.exit()
#get every option and run
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
#-h show full help function
        outputfullhelp()
        sys.exit()
    if opt_name in ('-v','--version'):
#-v show version(read custom config)
        try:
            f = open("binpython_config/version.py",encoding = "utf-8")
            exec(f.read())
            print("Powered by: BINPython[https://github.com/xingyujie/binpython] AGPL 3.0")
        except:
            print("BINPython " + ver + "-" + releases_ver + " By:XINGYUJIE[https://github.com/xingyujie/binpython] AGPL-3.0 LICENSE Release")
            print("Python " + platform.python_version())
        sys.exit()
    if opt_name in ('-f','--file'):
#-f runfile(or no option)
        file = opt_value
        f = open(file,encoding = "utf-8")
        exec(f.read())
        sys.exit()
    if opt_name in ('-s','--server'):
#-s set simple http server(support html or files transfer)
        server_port = opt_value
        webbrowser.open(f"http://127.0.0.1:{server_port}")
        exec("""
PORT = """ + server_port + """

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
""")
    if opt_name in ('-g','--gui'):
#-g gui show gui about info(based on tkinter)
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
#tkinter ide Simulation environment
    if opt_name in ('-i','--idle'):
        import tkinter as tk
        from tkinter import *
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
        sys.exit()
#-p binpython ideplus
    if opt_name in ('-p','--plus'):
        ideplusport = opt_value
        import pywebio.input
        from pywebio.input import *
        from pywebio.output import *
        from pywebio import *
        from pywebio.session import *
        import sys
        import subprocess
        import os
        import webbrowser
        print("______________________________________")
        print("BINPython WEB IDE STARTED")
        print(f"""
Welcome to BINPython IDEPlus!
HTTP Port: {ideplusport}
""")
#open browser
        webbrowser.open(f"http://127.0.0.1:{ideplusport}")
        #IDE Plus main
        def line():
            put_text('_______________________',
                sep=' '
            )
#set bootstrap ui(bar)
        def head():
            set_env(title="BINPython IDE Plus", auto_scroll_bottom=True)
            put_html(f"""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="http://localhost:{ideplusport}"></a>
    <img src="https://github.com/xingyujie/binpython/blob/main/py.ico?raw=true" width="30" height="30" class="d-inline-block align-top" alt="">
    BINPython IDEPlus
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="http://localhost:{ideplusport}/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:{ideplusport}/?app=ideplus">IDEPlus</a>
      </li>
        </a>
    </ul>
  </div>
</nav>

""")
        def plushead():
            set_env(title="BINPython IDE Plus", auto_scroll_bottom=True)
            put_html(f"""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="http://localhost:{ideplusport}"></a>
    <img src="https://github.com/xingyujie/binpython/blob/main/py.ico?raw=true" width="30" height="30" class="d-inline-block align-top" alt="">
    BINPython IDEPlus
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:{ideplusport}/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="http://localhost:{ideplusport}/?app=ideplus">IDEPlus</a>
      </li>
        </a>
    </ul>
  </div>
</nav>

""")
        def aboutideplus():
            head()
            put_markdown("## About BINPython IDEPlus")
            put_markdown("""
BINPython is made by:

[xingyujie(Edward Hsing)](https://github.com/xingyujie)

AGPL-V3.0 Release

""")
        def welcomecard():
            put_html(f"""
  <div class="jumbotron">
  <h1 class="display-3">Welcome to BINPython!</h1>
  <p class="lead">This is a portable IDE environment for BINPython</p>
  <hr class="my-4">
  <p>Fast and portable, runs via BINPython</p>
  <p class="lead">
    <a class="btn btn-primary btn-lg" href="http://localhost:{ideplusport}/?app=ideplus" role="button">Try IDE Plus!</a>
  </p>
</div>
""")
#index ui
        def index():
            head()
            welcomecard()
            put_markdown("## Features")
            put_link("IDEPlus", url=f'http://localhost:{ideplusport}/?app=ideplus')
            line()
            put_link("About BINPython", url=f'http://localhost:{ideplusport}/?app=aboutideplus')
            line()
            put_link("View Code", url=f'http://localhost:{ideplusport}/?app=viewcode')
        def idehead():
            set_env(title="BINPython IDE Plus", auto_scroll_bottom=True)
            put_html("<h1>BINPython IDE Plus</h1>")
            put_text('Welcome to BINPython IDE Plus, Please type code',
                    sep=' '
                )
            line()
            toast("BINPython IDE Plus is a beta version. May be removed or changed in the future")
#ideplus
        def ideplus():
            plushead()
            idehead()
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
#view code
        def viewcode():
            plushead()
            viewcode_code = pywebio.input.input("Please input file path:")
            f = open(viewcode_code,encoding = "utf-8")
            put_code(f.read(), language='python')
        if __name__ == '__main__':
            start_server([index, ideplus, aboutideplus, viewcode], debug=True, port=ideplusport)
            pywebio.session.hold()
            config(title="BINPython") #pywebio global title
#binpython examples
    if opt_name in ('-e','--example'):
        print("Welcome to BINPython example")
        print("""
List of examples:
1.Turtle
2.Tkinter GUI
3.Tornado WEB Server
4.PywebIO WEB
5.Hello World
6.HTTP requests
7.BINPython() function example

        """)
        examplenum = input("Please enter the option you want to enter(like 1):")
#turtle
        if examplenum == "1":
            def exampleturtle():
                import turtle
                import time
                turtle.speed(10)
                turtle.color("red", "yellow")
                turtle.begin_fill()
                for _ in range(50):
                    turtle.forward(200)
                    turtle.left(170)
                turtle.end_fill()
                turtle.done()
            exampleturtle()
            sys.exit()
#tkinter
        if examplenum == "2":
            def exampletkinter():
                import tkinter as tk
                app = tk.Tk()
                app.title('BINPython tkinter example')
                theLabel = tk.Label(app, text='Welcome to BINPython!!!') 
                theLabel.pack()
                app.mainloop()
            exampletkinter()
            sys.exit()
#tornado
        if examplenum == "3":
            def exampletornado():
                import asyncio
                import tornado.web
                class MainHandler(tornado.web.RequestHandler):
                    def get(self):
                        self.write("Hello, BINPython!")
                def make_app():
                    return tornado.web.Application([
                        (r"/", MainHandler),
                    ])
                async def main():
                    app = make_app()
                    app.listen(8080)
                    await asyncio.Event().wait()
                if __name__ == "__main__":
                    asyncio.run(main())
                    exit()
            print("Server Started listen on port:8080(http://ip:8080)")
            exampletornado()
            sys.exit()
#pywebio
        if examplenum == "4":
            import pywebio.input
            from pywebio.input import *
            from pywebio.output import *
            from pywebio import *
            from pywebio.session import *
            print("Listen on port 9000(http://ip:9000)")
            def examplepywebio():
                def main():
                    set_env(title="Welcome to BINPython", auto_scroll_bottom=True)
                    put_html("<h1>Welcome to BINPython</h1>")
                if __name__ == '__main__':
                    start_server(main, debug=True, host='0.0.0.0', port='9000')
                    pywebio.session.hold()
            examplepywebio()
            sys.exit()
#helloworld
        if examplenum == "5":
            binpythonwin.setwindowtitle("Hi, Welcome to BINPython")
            name = input("hi...What's your name:")
            print("hi," + name)
            sys.exit()
#requests
        if examplenum == "6":
            import requests
            def examplerequests():
                print(requests.get("http://google.com"))
            examplerequests()
            sys.exit()
#binpython function
        if examplenum == "7":
            print("BINPython() function example")
            import time
            binpythoninfo.ver()
            binpythoninfo.buildversion()
            binpythoninfo.libs_warning()
            binpythoninfo.build_importlibs()
            binpythonwin.setwindowtitle("Title name(str)")
            binpythonallconf()
            time.sleep(5)
            #main shell
            binpython_shell()
            sys.exit()

    if opt_name in ('-c','--cloudrun'):
        
        print("Welcome to CloudRun CLI. Let your script run in the cloud with BINPython")
        print('Type "help" for help information')
        while True:
            cloudruncli = input("cloudrun~ ")
            if cloudruncli == 'help':
                print("""
CloudRun Help:
get -- Enter application/script name to get run from software repository
load -- Run scripts from custom URL
version -- CloudRun Version
help -- run this help             
                """)
            if cloudruncli == 'get':
                print("Get apps/scripts in software repository")
                print("Under normal circumstances, we review the code of the software repositories and generally do not have any malware. But we will not take any legal responsibility")
                print()
                pkgname = input("packagename: ")
                cloudrun.get(pkgname)
            if cloudruncli == 'load':
                print("Let CloudRun run scripts through a custom server")
                print("The format should be like this: http://domain.com/filename.py")
                url = input("Python script URL: ")
                cloudrun.load(url)
            if cloudruncli == 'version':
                print(f"CloudRun-{cloudrunver} BINPython version By:Edward Hsing(xingyujie) AGPL-3.0 LICENSE")
            if cloudruncli == '':
                pass
            else:
                pass
            
#go main shell
#custom welcome script
try:
    f = open("binpython_config/welcome.py",encoding = "utf-8")
    exec(f.read())
    print("Powered by: BINPython[https://github.com/xingyujie/binpython] AGPL 3.0")
except:
    binpython_welcome_text()
#debug mode show many info
try:
    f = open("binpython_debug",encoding = "utf-8")
    print("Debug mode:on")
    print("BINPython debug INFO")
    def TestPlatform():
        import platform
        print(platform.python_version())
        print(platform.architecture())
        print(platform.node())
        print(platform.platform())
        print(platform.processor())
        print(platform.python_build())
        print(platform.python_compiler())
        print(platform.python_implementation())
        print(platform.python_revision())
        print(platform.release())
        print(platform.system())
        print(platform.version())
        print(platform.uname())
    TestPlatform()
except:
    pass
#binpython custom function plugin 
#plugin start
class binpythonplugin:
    plugin_name = ''
    def name(key):
        global plugin_name
        plugin_name = key
    #print(plugin_name)
    plugin_anthor = ''
    def anthor(key):
        global plugin_anthor
        plugin_anthor = key
    #description
    plugin_description = ''
    def description(key):
        global plugin_description
        plugin_description = key
    def showinfo():
        print("BINPython Plugin Info:")
        print("Plugin Name: " + plugin_name)
        print("Plugin Anthor: " + plugin_anthor)
        print("Plugin description: " + plugin_description)
    plugin_loadmain = ''
    def loadmain(key):
        global plugin_loadmain
        plugin_loadmain = key

#binpython_plugin_loadmain("function.py")
try:
    f = open("binpython_plugin/pluginconfig.binpython",encoding = "utf-8")
    exec(f.read())
    f = open("binpython_plugin/" + plugin_loadmain,encoding = "utf-8")
    exec(f.read())
    binpython_shell()
except:
    pass
try:
    filename = open("startupfile.conf",encoding = "utf-8")
    startupcode = open(filename.read(),encoding = "utf-8")
    exec(startupcode.read())
except:
    pass
#go shell
binpython_shell()