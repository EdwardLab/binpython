binpythonplugin.name("BINPython demo plugin")
binpythonplugin.anthor("Edward")
binpythonplugin.description("Simple BINPython example")

import os
class binpython_demo():
    def hello():
        print("hello BINPython")
    def linuxuname():
        os.system("uname -a")
    def winver():
        os.system("winver")