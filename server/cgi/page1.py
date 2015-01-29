#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
birthdate = form.getvalue('birthdate')
mainhobby = form.getvalue('mainhobby')

print """Content-type: text/html

<html><head><title>Page 2 (so original)</title></head><body>
Birthdate: %s / Main Hobby: %s

<br/>

<form method="post" action="page2.py">
Name:<textarea name="name" cols="40" rows="1"></textarea>

<br/>

Family:<textarea name="family" cols="40" rows="1"></textarea>

<br/>
<input type="submit" value="Submit">
</form>
</body></html>""" % (birthdate, mainhobby)