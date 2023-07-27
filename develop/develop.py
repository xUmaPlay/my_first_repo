# import requests
#
# url = "https://www.example.com"  # Замените на желаемый сайт
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Ошибка при выполнении запроса.")
#
# """
# # 2
# """
# import requests
#
# url = "https://www.example.com"  # Замените на желаемый сайт
# data = {"aiba": "shaiba", "danel": "ia"}  # Замените на данные, которые хотите отправить
#
# response = requests.post(url, data=data)
#
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Ошибка при выполнении запроса.")

"""
# 3
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def run_server():
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущен на localhost:8080")
    httpd.serve_forever()

run_server()