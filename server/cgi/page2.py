#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
family = form.getvalue('family')

print """Content-type: text/html

<html><head><title>Page 2 (so original)</title></head><body>
Name: %s / Family: %s

<br/>

<form method="post" action="page1.py">
Birthdate: <textarea name="birthdate" cols="40" rows="1"></textarea>

<br/>

Main Hobby: <textarea name="mainhobby" cols="40" rows="1"></textarea>

<br/>
<input type="submit" value="Submit">
</form>
</body></html>""" % (name, family)