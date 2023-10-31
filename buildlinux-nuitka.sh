#!/bin/bash


nuitka3 --standalone --onefile --enable-plugin=tk-inter  \
 --follow-imports --include-package-data=pywebio binpython.py
