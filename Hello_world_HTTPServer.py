__import__('http.server').server.HTTPServer(('', 80), (lambda s: (setattr(s, 'do_GET', lambda self: (self.send_response(200), self.send_header('Content-type', 'text/html'), self.end_headers(), self.wfile.write(b'Hello world!'))), s))(__import__('http.server').server.SimpleHTTPRequestHandler)[1]).serve_forever()
