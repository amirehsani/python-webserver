from http.server import HTTPServer, BaseHTTPRequestHandler
import time


HOST = "127.0.0.1"
PORT = 9999


class MyHTTP(BaseHTTPRequestHandler):

	# override
	# this function specifies how we handle GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(bytes("<html><body><h1> Hello World! </h1></body></html>", "utf-8"))

	# override
	# handling POST requests
	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers

		# some instruction




server = HTTPServer((HOST, PORT), MyHTTP)
print(f"Server is running on {HOST}:{PORT}")

server.serve_forever()


