<div align=center><img src="py.ico" width="  "></div>
<h1 align="center" name="binpython">BINPython</h1>
<p align="center">
    <em>Lightweight and small portable Python, build with pyinstaller
</em>
</p>
<p align="center">

![Github stars](https://img.shields.io/github/stars/xingyujie/binpython.svg)
![Discord](https://img.shields.io/badge/Discord-https://discord.gg/dz9HwwdSXh-green)
![telegram](https://img.shields.io/badge/Telegram-@binpython-blue)
![pyver](https://img.shields.io/badge/PythonVersion-<3.5-green)
![license](https://img.shields.io/badge/LICENSE-AGPL--3.0-brightgreen)
![author](https://img.shields.io/badge/Author-xingyujie-orange)
### Discord: https://discord.gg/dz9HwwdSXh
### Telegram: @binpython
### Twitter: xyj_offical
# Why BINPython?

Because:  
* no edit to registry  
* no extra .dlls（only a single executable）  
* licensed with AGPL-V3.0  
* Easy to integrate into any program, allowing any .py file to run without compiling to an executable  
* Built-in portable IDE environment, you can enjoy the highlighted standardized IDE without downloading additional IDE 
* Built-in portable http server for fast file transfer 
* Built-in tkinter and turtle GUI form application framework to quickly build compile-free form applications 
* Built-in dynamic website running framework such as tornado pywebio, the server is carried with you 
* Support to encapsulate any library into BINPython, take it with you wherever you go 
* The program occupies a small storage space, only about 10mb
# Usage
```
Usage: binpython [OPTIONS]

Options:

-h            --help               View this help
-f <filename> --file=<filename>    Enter Python Filename and run (*.py)
-s <port>     --server=<port>      Start a simple web server that supports html and file transfer (http.server)
-v            --version            View BINPython Version
-g            --gui                View GUI About and build info
-i            --idle               Open BINPython IDLE Code Editor

Additional options for the plus version

-p            --plus               Open BINPython IDE Plus Code Editor(beta) with http web server
-e            --example            Run various code examples through BINPython
```
# Build

1. Clone this project
```bash
git clone https://github.com/xingyujie/binpython
cd binpython
```
2. Install Python, pip and the pyinstaller environment
```bash
pip install pyinstaller
```
3. choose BINPython version to build
The standard version is for integration into programs.  It is recommended to use the ideplus version for learning 

## Build BINPthon Standard version
```bash
Windows: double-click "buildwin.bat" 

Linux: Go to terminal and run "buildlinux.sh" bash script 

(You can also use more compilation parameters, see pyinstaller documentation for details) 
```

4. Switch to the dist directory and find the compiled executable file, such as exe or bin file 
# Use
Under most Unix-like systems, run "./binpython" to run, double-click to run under Windows
