# server.py
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Name of the file to write
OUTPUT_FILENAME = 'my_blog_selection.json'

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/save-selection':
            return self.send_error(404)

        # Read incoming JSON
        length = int(self.headers.get('Content-Length', 0))
        body   = self.rfile.read(length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return self.send_error(400, "Invalid JSON")

        # Write to disk next to server.py
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Respond with success
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        resp = {'message': f'Saved to {OUTPUT_FILENAME}'}
        self.wfile.write(json.dumps(resp).encode('utf-8'))

if __name__ == '__main__':
    PORT = 8000
    os.chdir(os.path.dirname(__file__))  # serve files from this folder
    httpd = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f'→ Serving at http://localhost:{PORT}/')
    httpd.serve_forever()