# BINPython
Lightweight and small portable Python, build with pyinstaller
# Usage
```
-h     --help     View this help
-f     --file=     Enter Python Filename and run
-v     --version  View BINPython Version
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
3. Compile with basic pyinstaller, e.g.
```bash
pyinstaller -F binpython.py
```
(You can also use more compilation parameters, see pyinstaller documentation for details)

4. Switch to the dist directory and find the compiled executable file, such as exe or bin file 
# Use
Under most Unix-like systems, run "./binpython" to run, double-click to run under Windows
