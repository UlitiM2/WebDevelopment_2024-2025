import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
print(f'Запуск сервера на {server_address}')
server_socket.bind(server_address)

server_socket.listen(1)

while True:
    print('Ожидание соединения...')
    connection, client_address = server_socket.accept()

    try:
        print(f'Подключено новое соединение от {client_address}')

        data = connection.recv(1024).decode('utf-8')
        if data:
            print(f'Полученное сообщение: {data}')

            response_message = 'Hello, client'
            connection.sendall(response_message.encode('utf-8'))
            print(f'Отправлено сообщение: {response_message}')

    finally:
        connection.close()
