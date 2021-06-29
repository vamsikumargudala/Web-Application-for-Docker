#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

#Fieldstorage take input from the web browser
f = cgi.FieldStorage()
cmd = f.getvalue("x")

output = subprocess.getoutput("sudo " + cmd)
print(output)
