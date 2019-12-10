# coding=utf-8
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi


class PostHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         }
            )
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Client: %sn ' % str(self.client_address))
            self.wfile.write('User-agent: %sn' % str(self.headers['user-agent']))
            self.wfile.write('Path: %sn' % self.path)
            self.wfile.write('Form data:n')
            for field in form.keys():
                field_item = form[field]
                filename = field_item.filename
                filevalue = field_item.value
                filesize = len(filevalue)  # 文件大小(字节)
                # print len(filevalue)
                # print (filename)
                with open(filename.decode('utf-8'), 'wb') as f:
                    f.write(filevalue)
            return


        def StartServer():
            sever = HTTPServer(("", 8080), PostHandler)
            sever.serve_forever()



if __name__ == '__main__':
        PostHandler.StartServer()
'''
'''
from os import curdir
from os.path import join as pjoin

from http.server import BaseHTTPRequestHandler, HTTPServer

class StoreHandler(BaseHTTPRequestHandler):
    store_path = pjoin(curdir, 'Demo Transcript.txt')

    def do_GET(self):
        if self.path == 'Demo Transcript.txt':
            with open(self.store_path) as fh:
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                self.wfile.write(fh.read().encode())

    def do_POST(self):
        if self.path == 'Demo Transcript.txt':
            length = self.headers['content-length']
            data = self.rfile.read(int(length))

            with open(self.store_path, 'w') as fh:
                fh.write(data.decode())

            self.send_response(200)


server = HTTPServer(('', 8080), StoreHandler)
server.serve_forever()

import os
try:
    import http.server as server
except ImportError:
    # Handle Python 2.x
    import SimpleHTTPServer as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """Extend SimpleHTTPRequestHandler to handle PUT requests"""
    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        filename = os.path.basename('/static/')

        # Don't overwrite files

        if os.path.exists(filename):
            self.send_response(409, 'Conflict')
            self.end_headers()
            reply_body = '"%s" already exists\n' % filename
            self.wfile.write(reply_body.encode('utf-8'))
            return

        file_length = int(self.headers['Content-Length'])
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

if __name__ == '__main__':
    from http.server import BaseHTTPRequestHandler, HTTPServer
    server = HTTPServer(('127.0.0.1', 8080), HTTPRequestHandler)
    server.serve_forever()
    #server.test(HandlerClass=HTTPRequestHandler)
'''

#!/usr/bin/env python

"""Extend Python's built in HTTP server to save files

curl or wget can be used to send files with options similar to the following

  curl -X PUT --upload-file somefile.txt http://localhost:8000
  wget -O- --method=PUT --body-file=somefile.txt http://localhost:8000/somefile.txt

__Note__: curl automatically appends the filename onto the end of the URL so
the path can be omitted.

"""
#from http.server import HTTPServer, BaseHTTPRequestHandler
from BasicHttpServer import HTTPServer
#BasicHTTPRequestHandler
import os
import getinfo
try:
    import http.server as server
except ImportError:
    # Handle Python 2.x
    import SimpleHTTPServer as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    """Extend SimpleHTTPRequestHandler to handle PUT requests"""

    def do_PUT(self):
        """Save a file following a HTTP PUT request"""
        filename = os.path.basename(self.path)

        # Don't overwrite files
        '''
        if os.path.exists(filename):
            self.send_response(409, 'Conflict')
            self.end_headers()
            reply_body = '"%s" already exists\n' % filename
            self.wfile.write(reply_body.encode('utf-8'))
            return
        '''
        #file_length = int(self.headers['Content-Length'])
        #with open(filename, 'r')as output_file:
        #lst = getinfo.Solution.simplify(self,filename)
        score = getinfo.main(filename)
        #score = getinfo.Solution.getinfo(self,lst,'COURSES','ENG')
        #self.send_response(200)
        self.send_header("Content-type", "text/html")
        #score = getinfo.main(filename)
        self.send_response(201, 'Created')
        self.end_headers()
        self.wfile.write(bytes(score, "utf-8"))


if __name__ == '__main__':

    httpd = HTTPServer(('', 80), HTTPRequestHandler)
    print("=======1")
    print("Server started on local port 80.....")
    httpd.serve_forever()
    print("======2")
    #server.test(HandlerClass=HTTPRequestHandler)