import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
print(f'Подключение к {server_address}')
client_socket.connect(server_address)

try:
    message = 'Hello, server'
    print(f'Отправленное сообщение: {message}')
    client_socket.sendall(message.encode('utf-8'))

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print(f'Полученное сообщение: {data.decode("utf-8")}')
finally:
    print('Закрытие соединения с сервером')
    client_socket.close()
