from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        print('client', self.client_address)
        print('server', self.server)
        self.send_response(200)
    def do_PUT(self):
        """Respond to a PUT request."""

        file_name = os.path.basename(self.path)
        
        if os.path.exists(file_name):
            self.send_response(409, 'conflict')
            self.end_headers()
            reply_body = '"%s" already exists\n' % file_name
            self.wfile.write(reply_body.encode('utf-8'))
            return

        file_length = int(self.headers['Content-Length'])
        read = 0
        with open(file_name, 'wb+') as output_file:
            while read < file_length:
                new_read = self.rfile.read(min(66556, file_length - read))
                read += len(new_read)
                output_file.write(new_read)
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % file_name
        self.wfile.write(reply_body.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()