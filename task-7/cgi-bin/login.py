#!/usr/bin/python3

print("content-type:text/html")
print()


import cgi
import subprocess 

a = [""]
b = [""]

form = cgi.FieldStorage()
user  = form.getvalue('user')
password = form.getvalue('password')

if(user in a):
    if(password in b):
        final = subprocess.getoutput("cat /var/www/html/docker.html")
    else:
        print("invalid password")

else:
    print("invalid username")

print(final)

