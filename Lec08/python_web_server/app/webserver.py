import socket

HOST, PORT = '', 9000

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode('utf-8')
    print(request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()