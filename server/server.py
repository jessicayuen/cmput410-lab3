#!/usr/bin/env python
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8888)
handler.cgi_directories = ["/cgi"]

httpd = server(server_address, handler)
print "Starting server ..."
httpd.serve_forever()