import http.server


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """HTTP GET 요청을 처리한다."""
        self.route()

    def route(self):
        """요청 URL의 path에 따라 요청을 처리할 함수를 중계한다."""
        if self.path == '/hello':
            self.hello()
        else:
            self.response_404_not_found()

    def hello(self):
        """200 OK 상태 코드와 인사말을 응답한다."""
        self.response(200, '안녕하세요?')

    def response(self, status_code, body):
        """응답 메시지를 전송한다."""
        self.send_response(status_code)

        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write(body.encode('utf-8'))


ADDRESS = 'localhost', 8000

listener = http.server.HTTPServer(ADDRESS, HTTPRequestHandler)
print(f'http://{ADDRESS[0]}:{ADDRESS[1]} 주소에서 요청 대기중...')
listener.serve_forever()
