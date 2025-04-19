import socket


def calculate_trapezoid_area(a, b, h):
    if a > 0 and b > 0 and h > 0:
        return ((a + b) / 2) * h
    else:
        return 'error'


def handle_client(conn, addr):
    print(f'Подключение к {addr}')

    while True:
        data = conn.recv(1024).decode('utf-8')

        if not data:
            break

        try:
            a, b, h = map(float, data.split(','))
            result = calculate_trapezoid_area(a, b, h)
            response = f'Площадь трапеции: {result:.2f}'
            conn.sendall(response.encode('utf-8'))
        except ValueError as e:
            error_message = f'Ошибка ввода: {e} '
            conn.sendall(error_message.encode('utf-8'))

    conn.close()


if __name__ == '__main__':
    HOST = ''
    PORT = 11111

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Ожидание соединения...')

        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)
