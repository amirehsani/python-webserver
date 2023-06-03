from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHTTP(BaseHTTPRequestHandler):

    # override
    # this function specifies how we handle GET requests
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html><body><h1> Hello World! </h1></body></html>", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes("404 Not Found", "utf-8"))

    # override
    # handling POST requests
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")

        # Process the post_data as needed
        # ...

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(bytes("POST request processed", "utf-8"))


def run(server_class=HTTPServer, handler_class=MyHTTP, host="localhost", port=8020):
    server_address = (host, port)
    my_server = server_class(server_address, handler_class)
    print(f"Server is running on {host}:{port}")
    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        my_server.server_close()
        print("Server stopped")


if __name__ == "__main__":
    run()
