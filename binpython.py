#BINPython AGPL-V3.0 LICENSE Release
#Under the AGPL-V3 license
#full version


####################################
#build configure

ver = "0.46"
libs_warning = "1"
#1 is ture 0 is false.
#Changing the value to 0 will close the prompt that the library does not exist


releases_ver = "official"
importlibs = "" # For custom imported libraries before building, use "," to separate them (must be installed in the native Python before building), or directly use import <library> to add to the list below, example: importlibs = "os,sys,wget,flask"
cloudrunver = "1.04"
cmdver = "0.08"

####################################

#BINPython function and variable START

class binpythoninfo:
    def ver():
        print(ver)

    def libs_warning():
        print(libs_warning)

    def releases_ver():
        print(releases_ver)

    def build_importlibs():
        print(importlibs)
from os import makedirs
import time
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
    print("ver: " + ver + " buildversion: " + " libs_warning settings:" + libs_warning + " releases full version: " + releases_ver + " custom library that has been build: " + importlibs)
#if system is windows, show default window title
if sys == "Windows":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("BINPython " + ver)
try:
    if importlibs != '':
        import importlib
        libraries = importlibs.split(",")
        for lib in libraries:
            importlib.import_module(lib)
#get libswarning
except ImportError as e:
    if libs_warning == "1":
        print("Warning: Custom import library %s does not exist, please check the source code library configuration and rebuild" % importlibs)
        print("Error: " + str(e))
        print("")
#run python files option(-f)
def optreadfile():
    import sys
    getfile = sys.argv[1]
    getfilecode = open(getfile,encoding = "utf-8")
    exec(getfilecode.read())
    sys.exit(0)
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
    import base64
    import cmd
    import zipfile
    import requests
    import urllib
    import wget
    import shutil
    import json
    import rich
    from rich.console import *
    from rich.markdown import *
    from rich.syntax import *
#fix for exit()
    from sys import exit
#import for http_server
    import http.server
    import socketserver
    from flask import Flask, render_template, request, redirect, url_for
    from flask_login import LoginManager, current_user, login_required, UserMixin, login_user, logout_user
    from werkzeug.security import generate_password_hash, check_password_hash
    from werkzeug.utils import secure_filename
#except ImportError:
except(Exception, BaseException) as error:
    print("Unable to use any library, the program does not work properly, please rebuild")
    f = open("binpython_importerror.log", "a")
    f.write('Import Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
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
    import pyautogui
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
    import email.mime.message
    import email.mime.application
    import email.mime.audio
    import email.mime.base
    import email.mime.image
    import email.mime.multipart
    import email.mime.text
    import email.mime.nonmultipart
    import sqlite3
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
    print("BINPython " + ver + "-" + releases_ver + " Python " + platform.python_version() + " [Running on " + platform.platform() + " " + platform.version() + "]")
    print('Type "about", "help", "copyright", "credits" or "license" for more information. Type "binpython_cmd()" to enter BINPython CMD')
def binpython_shell():
    while True:
        try:
            pycmd=input(">>> ")
            if pycmd in globals().keys():
                print(globals()[pycmd])
                continue
            elif pycmd == 'about':
                print("BINPython By: Edward Hsing[https://github.com/xingyujie] AGPL-3.0 LICENSE Release")
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
            elif pycmd == 'binpython_cmd':
                binpython_cmd()
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


def cloudruncli():
           
        print("Welcome to CloudRun CLI. Let your script run in the cloud with BINPython")
        print('Type "help" for more information')
        while True:
            cloudruncli = input("cloudrun~ ")
            if cloudruncli == 'help':
                print("""
CloudRun Help:
get -- Enter application/script name to get run from software repository
load -- Run scripts from custom URL
editsource -- Set up custom sources and save via configuration files
shell -- Go to BINPython Shell
version -- CloudRun Version
help -- show this help    
exit -- quit cloudrun         
                """)
            if cloudruncli == 'get':
                print("Get apps/scripts in software repository")
                print("Under normal circumstances, we review the code of the software repositories and generally do not have any malware. But we will not take any legal responsibility")
                print()
                pkgname = input("packagename: ")
                if pkgname == '':
                    pass
                else:
                    cloudrun.get(pkgname)
            if cloudruncli == 'load':
                print("Let CloudRun run scripts through a custom server")
                print("The format should be like this: http://domain.com/filename.py")
                url = input("Python script URL: ")
                if url == '':
                    pass
                else:
                    cloudrun.load(url)
            if cloudruncli == 'editsource':
                print('caution! The set software source must be in a standard format, otherwise it may not work, like http://127.0.0.1/, if you set http://127.0.0.1, it will not work properly, even if there is one less "/"!')
                entersource = input("Please input sources server address: ")
                cloudrun.editsource(entersource)
                print("success!")
            if cloudruncli == 'shell':
                binpython_shell()
            if cloudruncli == 'version':
                print(f"CloudRun-{cloudrunver} BINPython version By:Edward Hsing(Xing Yu Jie) AGPL-3.0 LICENSE")
            if cloudruncli == 'exit':
                exit()
            if cloudruncli == '':
                pass
            else:
                pass
class cloudrun:
    def get(pkgname):
        try:
            sources = open("cloudrun_config/sources.config", "r")
            sources = str(sources.read()) + pkgname + ".py"
        except:
            sources = f"https://raw.githubusercontent.com/xingyujie/cloudrun-repository/main/{pkgname}.py"
        try:
            cloudrunenv = True
            getcoderes = urllib.request.urlopen(sources)
        except(Exception, BaseException) as error:
            print("There is no network connection or the repository does not exist for this script")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write('Get Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        try:
            exec(str(getcoderes.read().decode('utf-8')))
            getcoderes.close()
        except(Exception, BaseException) as error:
            print("run failed")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write('Run Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
    def load(url):
        try:
            cloudrunenv = True
            getcoderes = urllib.request.urlopen(url)
        except(Exception, BaseException) as error:
            print("There is no network connection or the repository does not exist for this script")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write('Get Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        try:
            exec(getcoderes.read().decode('utf-8'))
            getcoderes.close()
        except(Exception, BaseException) as error:
            print("run failed")
            print("Error details are in cloudrun_error.log in the run directory")
            f = open("cloudrun_error.log", "a")
            f.write('Run Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
    def editsource(url):
        try:
            os.mkdir("cloudrun_config")
        except:
            pass
        sources = open("cloudrun_config/sources.config", "w")
        sources.write(url)
    
#cloudrun functions end

#cmd start
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
def listfiles():
    import os
    dirs = os.listdir("./")
    for file in dirs:
        print (file)
def listfilesfunc(path):
    import os
    dirs = os.listdir(path)
    for file in dirs:
        print (file)
def download(url,path):
    if not os.path.exists(path):
         os.mkdir(path)
    start = time.time()
    response = requests.get(url, stream=True)
    size = 0  
    chunk_size = 1024 
    content_size = int(response.headers['content-length'])
    try:
        if response.status_code == 200:
            print('Start download,[App size]:{size:.2f} MB'.format(size = content_size / chunk_size /1024)) 
            filepath = path+'\name.extension name'
            with open(filepath,'wb') as file:
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[Downloading]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time() 
        print('Download completed!,times: %.2f second' % (end - start))
    except:
        print("Download package failed!")
def unzip(path, folder_abs):
    zip_file = zipfile.ZipFile(path)
    zip_list = zip_file.namelist() 

    for f in zip_list:
        zip_file.extract(f, folder_abs)
 
    zip_file.close()
def mkbpfs():
    print("Welcome to bpfs[BINPython File System] making tool (mkfs.bpfs). Type help to list commands and help.")
    while True:
        cmd = input("(BPFS CLI) ")
        if cmd == 'mkfs':
            print("Make a new bpfs filesystem")
            fspath = input("Enter the bpfs save path of the file system: ")
            try:
                os.mkdir(fspath)
            except:
                pass
            try:
                os.chdir(fspath)
                print("[*] Done.")
            except:
                print("[E] path does not exist!")
            print("[*] Make base file system")
            try:
                os.makedirs("binpython_files/apps")
                os.makedirs("binpython_files/cmd")
                os.makedirs("binpython_files/hostname")
                os.makedirs("binpython_files/userdata")
                open("binpython_files/cmd/cmd.py", "w")
            except(Exception, BaseException) as error:
                print("make dirs and files Error." + error)
            try:
                hostnameyn = input("do you want to create hostname(y/n): ")
                if hostnameyn == 'y':
                    hostnamecontent = input("enter hostname: ")
                    with open("binpython_files/hostname/hostname", "w") as sethostname:
                        sethostname.write(hostnamecontent)
                    print("[*] Done.")
                else:
                    pass
            except(Exception, BaseException) as error:
                print("makehostname Error." + error)
            try:
                usernameyn = input("do you want to set default login user(y/n): ")
                if usernameyn == 'y':
                    usernamecontent = input("enter default login username: ")
                    with open("binpython_files/userdata/defaultloginuser", "w") as setusername:
                        setusername.write(usernamecontent)
                    os.makedirs(f"binpython_files/userdata/home/{usernamecontent}")
                    print("[*] Done.")
                else:
                    pass
            except(Exception, BaseException) as error:
                print("Set default username Error. " + error)
        if cmd == 'help':
            print("""
List commands:
mkfs -- Make a new bpfs filesystem
help -- This help
exit -- exit mkbpfs
            """)
        if cmd == 'exit':
            binpython_cmd()
def getfsfile(path):
    try:
        os.mkdir("binpython_files")
    except:
        pass
        print("[*] Unzip File System BPFS(BINPython File System) from file")
        unzip(path, runpath + "/binpython_files")
        print("\n")
        print("[*] Done!")
        binpython_cmd()
def downfs(bpfsurl):
    try:
        os.mkdir("binpython_files")
    except:
        pass
        print("[*] Download File System BPFS(BINPython File System)")
        wget.download(bpfsurl, runpath + "/binpython_files")
        unzip(runpath + "/binpython_files/officialbpfsbase.bpfs", runpath + "/binpython_files")
        print("\n")
        print("[*] Done!")
        binpython_cmd()
def pkg_inst_ask():
    try:
        input("Enter to continue")
    except:
        sys.exit()

    
def binpython_cmd():
    global runpath
    os.system('cls' if os.name == 'nt' else 'clear')
    runpath = os.path.dirname(os.path.realpath(sys.argv[0]))
    time.sleep(3)
    try:
        os.chdir(runpath + f"/binpython_files/userdata/")
        os.chdir(runpath + f"/binpython_files/cmd")
    except:
            print('''
Welcome to BINPython CMD!
The file system cannot be found or there is an incomplete file system.
type "getfs" to download a file system;
type "getfsurl" to download a filesystem via a custom url;
Type "getfsfile" to unzip the filesystem via file;
type "mkbpfs" to make a new file system;
type "exit" to exit;
type "shell" to force entry into the shell.
* After forcing into the shell, you can create bpfs via "mkbpfs" command or use "adduser", "setdefaultuser" and other commands to build the filesystem step by step. But we don't recommend it, it may be more problematic and more complex
    ''')
            while True:
                initcmd = input("(InstallationENV) ")
                if initcmd == 'exit':
                    exit()
                if initcmd == 'shell':
                    break
                if initcmd == 'mkbpfs':
                    mkbpfs()
                if initcmd == 'getfs':
                    downfs('https://raw.githubusercontent.com/xingyujie/binpython-repository/main/officialbpfsbase.bpfs')
                    print("Finish! please restart BINPython")
                    sys.exit()
                if initcmd == 'getfsurl':
                    fsurl = input("Please enter a download link (like: http://url.com/bpfs/bpfsbase.bpfs)")
                    downfs(fsurl)
                if initcmd == 'getfsfile':
                    filepath = input("Please enter a (*.bpfs) file path: ")
                    getfsfile(filepath)
    try:
        global cmd_username
        defaultprofile = open(runpath + "/binpython_files/userdata/defaultloginuser", "r")
        cmd_username = defaultprofile.read()
        os.chdir(runpath + f"/binpython_files/userdata/home/{cmd_username}")
    except:
        cmd_username = 'user'
        print('Unable to switch to BINPython userprofile: Default user not found. To use a temporary directory user, use "adduser" and "setdefaultuser <username>" to create a user and set default user')
        print()
    try:
        gethostname = open(runpath + "/binpython_files/hostname/hostname", "r")
        cmd_hostname = gethostname.read()
    except:
        cmd_hostname = "binpython"
    try:
        shutil.rmtree(runpath + f"/binpython_files/userdata/home/tempuser")
        shutil.rmtree(runpath + f"/binpython_files/apps/tempuser")
    except:
        pass
    class cmdshell(cmd.Cmd):
        intro = 'Welcome to BINPython Shell. Type help or ? to list commands and help.\n'
        prompt = cmd_username + '@' + cmd_hostname + ':~# '
        file = None
        try:
            os.makedirs(runpath + f"/binpython_files/cmd/")
        except:
            pass
        try:
            f = open(runpath + f"/binpython_files/cmd/cmd.py", "r")
            exec(f.read())
        except(Exception, BaseException) as error:
            f = open(runpath + f"/binpython_files/cmd/cmd_ignore.txt", "a")
            f.write('Custom CMD ignore: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_cloudrunget(self, arg):
            'Get CloudRun Script from repository use:cloudrunget <scriptname>'
            cloudrun.get(arg)        
        def do_cloudrunload(self, arg):
            'Get CloudRun Script from repository use:cloudrunload <URL> URL can be http://domain.com/filename.py'
            cloudrun.load(arg)
        def do_cloudruneditsource(self, arg):
            'Change the source of CloudRun'
            cloudrun.editsource(arg)
        def do_ls(self, arg):
            'List files'
            listfiles()
        def do_pwd(self, arg):
            'show current path'
            print(os.path.dirname(os.path.realpath('__file__')))
        def do_cd(self, arg):
            'change path'
            os.chdir(arg)
        def do_adduser(self, arg):
            'Create a new user profile for BINPython'
            print("Create a new user profile for BINPython")
            scriptpath = os.path.dirname(os.path.realpath(sys.argv[0]))
            username = input("Username: ")
            print("create user...")
            try:
                os.makedirs(runpath + f"/binpython_files/userdata/home/{username}")
            except(Exception, BaseException) as error:
                print("User already exits or system error")
                print(error)
            print("Done")
        def do_setdefaultuser(self, arg):
            'Set a default user. Usage: setdefaultuser <username>'
            defaultprofile = open(runpath + "/binpython_files/userdata/defaultloginuser", "w")
            defaultprofile.write(arg)
            print("Done")
        def do_shell(self, arg):
            'Go to Python interpreter'
            binpython_shell()
        def do_python(self, arg):
            'Run a Python script file (*.py) Usage: python <filename>.py'
            if arg == '':
                binpython_shell()
            f = open(arg, "r")
            exec(f.read())
        def do_seteditor(self, arg):
            'Set a default Python or Text file code editor usage: seteditor <editorname>. like: "seteditor code" (Open code via Visual Studio Code when using the "edit <filename>" command). "seteditor notepad" (Open the code through Notepad that comes with Windows)'
            defaulteditor = open(runpath + f"/binpython_files/userdata/home/{cmd_username}/defaulteditor.config", "w")
            defaulteditor.write(arg)
        def do_edit(self, arg):
            'Before using this command, you must use "seteditor <editorname>" to set the editor (see the usage of this parameter for details), otherwise it cannot be called up. edit usage: edit <filename>'
            try:
                defaulteditor = open(runpath + f"/binpython_files/userdata/home/{cmd_username}/defaulteditor.config", "r")
                os.system(defaulteditor.read() + ' ' + arg)
            except KeyboardInterrupt:
                pass
        def do_exit(self, arg):
            'exit shell'
            print("logout")
            sys.exit()
        def do_sethostname(self, arg):
            'set up hostname. Usage sethostname <hostname>'
            try:
                os.makedirs(runpath + "/binpython_files/hostname/")
            except:
                pass
            hostnamefile = open(runpath + "/binpython_files/hostname/hostname", "w")
            hostnamefile.write(arg)
        def do_rm(self, arg):
            'remove files Usage: rm <filename>'
            os.remove(arg)
        def do_system(self, arg):
            'call system command. Usage: system <command> like: system ls (Invoke system command to list directory)'
            os.system(arg)
        def do_mkdir(self, arg):
            'make a directory. Usage: mkdir <dirname>'
            os.mkdir(arg)
        def do_touch(self, arg):
            'make a empty file Usage: touch <filename>'
            open(arg, "w")
        def do_write(self, arg):
            'write text to file. Usage: write <filename>'
            writetext = open(arg, "w")
            arg1 = input(f"What you want to write to the target file {arg}: ")
            writetext.write(arg1)
        def do_uname(self, arg):
            'version of CMD'
            print(f"BINPython CMD By: Edward Hsing VER:{cmdver} ")
        def do_user(self, arg):
            'Switch User Usage: user <username>'
            os.chdir(runpath + f"/binpython_files/userdata/home/{arg}")
            try:
                f = open(runpath + "/binpython_files/userdata/defaultloginuser", "w")
                f.write(arg)
            except(Exception, BaseException) as error:
                print('Switch User Error, please see the log "binpython_user_error.log" for details')
                f = open("binpython_user_error.log", "a")
                f.write('Switch User Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_install(self, arg):
            'Install package'
            try:
                os.makedirs(runpath + f"/binpython_files/apps/{cmd_username}")
            except:
                pass
            try:
                os.makedirs(runpath + f"/binpython_files/apps/{cmd_username}/installtemp")
            except:
                pass
            try:
                global appsource
                f = open(runpath + f"/binpython_files/apps/source.config", "r")
                appsource = f.read()
            except:
                f = open(runpath + f"/binpython_files/apps/source.config", "w")
                f.write("https://raw.githubusercontent.com/xingyujie/binpython-repository/main/")
                appsource = "https://raw.githubusercontent.com/xingyujie/binpython-repository/main/"
            if arg == '':
                print("Please use install <package name> missing options <package name>")
                exit()
            try:
                print("[*] download package")
                wget.download(f"{appsource}{arg}.bpkg", runpath + f"/binpython_files/apps/{cmd_username}/installtemp/{arg}.bpkg")
                print("\n")
            except(Exception, BaseException) as error:
                print('The package does not exist or system error, please see the log "install_error.log" for details')
                f = open("install_error.log", "a")
                f.write('Install Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + f" {appsource}{arg}.bpkg " + str(error) +'\n')
                exit()
            try:
                print("[*] Unzip the package")
                unzip(runpath + f"/binpython_files/apps/{cmd_username}/installtemp/{arg}.bpkg", runpath + f"/binpython_files/apps/{cmd_username}/{arg}")
            except(Exception, BaseException) as error:
                print('Unzip the package failed, please see the log "install_error.log" for details')
                f = open("install_error.log", "a")
                f.write('Unzip package Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                f = open(runpath + f"/binpython_files/apps/{cmd_username}/{arg}/package.json")
                pkginfo = json.loads(f.read())
                print(f"""
Package information:
Name: {pkginfo['name']}
Version: {pkginfo['version']}
Summary: {pkginfo['summary']}
Homepage: {pkginfo['homepage']}
Author: {pkginfo['author']}  
Email: {pkginfo['email']}     
License: {pkginfo['license']}     
                """)
                f.close()
                pkg_inst_ask()
            except(Exception, BaseException) as error:
                print('[W] Warning: Could not find package configuration information file, please see the log "install_warning.log" for details')
                f = open("install_warning.log", "a")
                f.write('Run package information Warning: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                print("[*] configure package")
                f = open(runpath + f"/binpython_files/apps/{cmd_username}/{arg}/config.py")
                exec(f.read())
            except(Exception, BaseException) as error:
                print('[W] Warning: config file no configuration or configuration error, please see the log "install_warning.log" for details')
                f = open("install_warning.log", "a")
                f.write('Run package configuration file Warning: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                print("[*] Clean up temporary files")
                os.remove(runpath + f"/binpython_files/apps/{cmd_username}/installtemp/{arg}.bpkg")
            except(Exception, BaseException) as error:
                print('Failed to clean up temporary files, please see the log "install_error.log" for details')
                f = open("install_error.log", "a")
                f.write('clean up temporary files Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                os.removedirs(runpath + f"/binpython_files/apps/{cmd_username}/installtemp")
            except:
                pass
            print("[OK]Finished!")
        def do_installfile(self, arg):
            'Install package from local bpkg file'
            if arg == '':
                print("Please use install <package file name> missing options <package file name>")
                exit()
            nobpkgarg = arg.replace('.bpkg', '')
            try:
                os.makedirs(runpath + f"/binpython_files/apps/{cmd_username}")
            except:
                pass
            try:
                os.makedirs(runpath + f"/binpython_files/apps/{cmd_username}/installtemp")
            except:
                pass
            try:
                print("[*] Unzip the package")
                unzip(arg, runpath + f"/binpython_files/apps/{cmd_username}/{nobpkgarg}")
            except(Exception, BaseException) as error:
                print('Unzip the package failed, please see the log "install_error.log" for details')
                f = open("install_error.log", "a")
                f.write('Unzip package Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                f = open(runpath + f"/binpython_files/apps/{cmd_username}/{nobpkgarg}/package.json")
                pkginfo = json.loads(f.read())
                print(f"""
Package information:
Name: {pkginfo['name']}
Version: {pkginfo['version']}
Summary: {pkginfo['summary']}
Homepage: {pkginfo['homepage']}
Author: {pkginfo['author']}  
Email: {pkginfo['email']}     
License: {pkginfo['license']}     
                """)
                pkg_inst_ask()
            except(Exception, BaseException) as error:
                print('[W] Warning: Could not find package configuration information file, please see the log "install_warning.log" for details')
                f = open("install_warning.log", "a")
                f.write('Run package information Warning: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                print("[*] configure package")
                f = open(runpath + f"/binpython_files/apps/{cmd_username}/{nobpkgarg}/config.py")
                exec(f.read())
            except(Exception, BaseException) as error:
                print('[W]config file no configuration or configuration error, please see the log "install_warning.log" for details')
                f = open("install_warning.log", "a")
                f.write('Run package configuration file Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            try:
                os.removedirs(runpath + f"/binpython_files/apps/{cmd_username}/installtemp")
            except:
                pass
            print("[OK]Finished!")
        def do_switchappdir(self, arg):
            'Switch to App directory. Usage: switchappdir <appname>'
            try:
                os.chdir(runpath + f"/binpython_files/apps/{cmd_username}/{arg}")
            except(Exception, BaseException) as error:
                print('Can not switch app directory, please see the log "binpython_pkg_error.log" for details')
                f = open("binpython_pkg_error.log", "a")
                f.write('Switch package directory Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_runapp(self, arg):
            'To run a BINPython bpkg program, first pass install <app name> or installfile <app package path> Usage: runapp <appname>. '
            try:
                execpyfile(runpath + f"/binpython_files/apps/{cmd_username}/{arg}/main.py")
            except(Exception, BaseException) as error:
                print('App not exits or failed, please see the log "binpython_pkg_error.log" for details')
                f = open("binpython_pkg_error.log", "a")
                f.write('Run package Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_removeapp(self, arg):
            'To delete a BINPython application, usage: removeapp <appname>'
            try:
                shutil.rmtree(runpath + f"/binpython_files/apps/{cmd_username}/{arg}")
            except(Exception, BaseException) as error:
                print('App not exits or failed, please see the log "binpython_pkg_error.log" for details')
                f = open("binpython_pkg_error.log", "a")
                f.write('Remove package Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_listapps(self, arg):
            'List installed BINPython applications'
            try:
                listfilesfunc(runpath + f"/binpython_files/apps/{cmd_username}")
            except(Exception, BaseException) as error:
                print('Can not list apps, please see the log "binpython_pkg_error.log" for details')
                f = open("binpython_pkg_error.log", "a")
                f.write('List package Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_editsource(self, arg):
            'To change the software source, usage: editsouce <souceurl>. Please pay attention to the software source specification, otherwise you will get an error. <souceurl> like this: http://xxx.com/'
            f = open(runpath + f"/binpython_files/apps/source.config", "w")
            f.write('http://' + arg + '/')
        def do_tempuser(self, arg):
            'Create a temporary user, logging out will destroy the user space'
            print("You are trying to create a temporary user, this user space is only used for demonstration, testing and learning. When this user is logged out, all user data will also be deleted")
            print("..........")
            time.sleep(0.3)
            print('Please note: the username of the temporary user is "tempuser" and the "tempuser" user is being created')
            try:
                os.makedirs(runpath + f"/binpython_files/apps/tempuser")
                os.makedirs(runpath + f"/binpython_files/userdata/home/tempuser")
            except(Exception, BaseException) as error:
                print('Can not create tempuser, please see the log "binpython_user_error.log" for details')
                f = open("binpython_user_error.log", "a")
                f.write('Switch tempuser Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
            os.chdir(runpath + f"/binpython_files/userdata/home/tempuser")
            print("Created successfully, has switched to the tempuser directory")
        def do_repolist(self, arg):
            'Change the BINPython source from the official list'
            cloudrun.load("https://raw.githubusercontent.com/xingyujie/binpython-repository/main/source.py")
        def do_cloudrunshell(self, arg):
            'Go to CloudRun Shell'
            cloudruncli()
        def do_whoami(self, arg):
            'Print Username'
            print(cmd_username)
        def do_hostname(self, arg):
            'Print Hostname'
            print(cmd_hostname)
        def do_rootpath(self, arg):
            'Print rootpath(runpath)'
            print(runpath)
        def do_initcmd(self, arg):
            'Initialize the custom CMD command file. After opening, you can use the "def do_cloudrunget(self, arg):" code to write your own commands through the "/binpython_files/cmd/cmd.py" file.'
            try:
                os.makedirs(runpath + f"/binpython_files/cmd")
            except:
                pass
            try:
                f = open(runpath + f"/binpython_files/cmd/{arg}.py", "w")
                f.write('#Initialize the custom CMD command file, you can write your own command through the "def do_cloudrunget(self, arg):" code, please refer to "https://docs.python.org/3/library/cmd.html" for details')
            except(Exception, BaseException) as error:
                print('Can not initcmd, please see the log "binpython_cmd_error.log" for details')
                f = open("binpython_cmd_error.log", "a")
                f.write('Init CMD Error: ' + time.strftime('%m-%d-%Y %H:%M:%S',time.localtime(time.time())) + ' ' + str(error) + '\n')
        def do_mkbpfs(self, arg):
            'Make BINPython File System'
            mkbpfs()
    if __name__ == '__main__':
        cmdshell().cmdloop()
#cmd end

#def
#print all helpinfo
helpinfo = """
Usage: binpython [OPTIONS]

Options:
<filename>                         Enter a Python filepath and run the script (*.py) [or -f <filename>]
-h            --help               View this help documentation
-s <port>     --server=<port>      Start a simple web server that supports HTML and file transfer (using http.server)
-i            --idle               Launch the BINPython IDLE
-e            --example            Run library and code examples
-c            --cmd                BINPython CMD (Use the "help" command to view cmd help)
-v            --version            Print BINPython Version
"""

def custhelp():
    try:
        f = open("binpython_config/help.txt",encoding = "utf-8")
        print(f.read())
    except:
        print(helpinfo)
#set about info
about = "BINPython " + ver + "-" + releases_ver + " By: DigitalPlat Edward Hsing [https://github.com/xingyujie/binpython, http://digitalplat.org, http://binpython.org] AGPL-3.0 LICENSE Release"
#getopt
try:
#set options
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-s:-i-e-c-v',['help','file=','server=','idle','example','cmd','version'])
#set getopt error prompt
except getopt.GetoptError as err:
    print("Please check help:")
    print("Invalid gargument. Please check help.")
#show full help(custhelp())
    custhelp()
    sys.exit()
#get every argv
for opt_name,opt_value in opts:
    def execpyfile(filename):
        f = open(filename)
        exec(f.read())
    if opt_name in ('-h','--help'):
#-h show full help function
        custhelp()
        sys.exit()
    if opt_name in ('-v','--version'):
#-v show version(read custom config)
        try:
            f = open("binpython_config/version.py",encoding = "utf-8")
            exec(f.read())
            print("Powered by: BINPython[https://github.com/xingyujie/binpython] AGPL 3.0")
        except:
            print("BINPython " + ver + "-" + releases_ver + " By: DigitalPlat Edward Hsing [https://github.com/xingyujie/binpython, http://digitalplat.org, http://binpython.org] AGPL-3.0 LICENSE Release")
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
#tkinter ide Simulation environment
    if opt_name in ('-i','--idle'):
        import tkinter as tk
        from tkinter import *
        import os
        from tkinter import Menu
        from tkinter import messagebox

        def show():
            binpythonwin.setwindowtitle("BINPython IDLE Mode")
            code = e1.get(1.0, END)
            print("================= BINPython Restart =================")
            exec(code)

        def about():
            messagebox.showinfo("About BINPython IDLE", "Welcome to BINPython " + str(ver) + " Python Version: " + platform.python_version())

        def copy_text():
            selected_text = e1.get(SEL_FIRST, SEL_LAST)
            if selected_text:
                e1.clipboard_clear()
                e1.clipboard_append(selected_text)

        def cut_text():
            selected_text = e1.get(SEL_FIRST, SEL_LAST)
            if selected_text:
                e1.delete(SEL_FIRST, SEL_LAST)
                e1.clipboard_clear()
                e1.clipboard_append(selected_text)

        def paste_text():
            clipboard_text = e1.clipboard_get()
            if clipboard_text:
                e1.insert(INSERT, clipboard_text)

        def select_all():
            e1.tag_add("sel", "1.0", "end")

        def show_popup_menu(event):
            menu = tk.Menu(master, tearoff=0)
            menu.add_command(label="Copy", command=copy_text)
            menu.add_command(label="Cut", command=cut_text)
            menu.add_command(label="Paste", command=paste_text)
            menu.add_command(label="Select All", command=select_all)
            menu.post(event.x_root, event.y_root)

        master = tk.Tk()
        master.title("BINPython IDLE")

        # Set theme colors
        master.configure(bg="#1F1F1F")
        master.option_add('*TButton*highlightBackground', "#1F1F1F")
        master.option_add('*TButton*highlightColor', "#1F1F1F")

        # Create a menu bar
        menu = Menu(master)
        master.config(menu=menu)

        # Create a File menu
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Run", command=show)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=master.quit)

        # Create an Edit menu
        edit_menu = Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=copy_text)
        edit_menu.add_command(label="Cut", command=cut_text)
        edit_menu.add_command(label="Paste", command=paste_text)
        edit_menu.add_command(label="Select All", command=select_all)

        # Create a Help menu
        help_menu = Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=about)

        # Add a code input field
        e1 = Text(master, bg="#1F1F1F", fg="white")
        e1.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="nsew")

        # Bind right-click menu
        e1.bind("<Button-3>", show_popup_menu)

        # Add Run and Exit buttons
        run_button = tk.Button(master, text="Run", width=10, command=show, bg="#0078D4", fg="white")
        exit_button = tk.Button(master, text="EXIT", width=10, command=master.quit, bg="#0078D4", fg="white")
        run_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        exit_button.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        master.mainloop()

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
#helloworld basic func
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

    if opt_name in ('-c','--cmd'):
        binpython_cmd()
#go main shell
#custom welcome script
try:
    f = open("binpython_config/welcome.py",encoding = "utf-8")
    exec(f.read())
    print("Powered by: BINPython[https://github.com/xingyujie/binpython] AGPL 3.0")
except:
    pass
#debug mode show info
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
if len(sys.argv) == 1:
    binpython_welcome_text()
    binpython_shell()