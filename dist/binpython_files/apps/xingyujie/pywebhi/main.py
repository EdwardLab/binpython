from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info


name = input("What's your name")
print("Your name is %s" % name)