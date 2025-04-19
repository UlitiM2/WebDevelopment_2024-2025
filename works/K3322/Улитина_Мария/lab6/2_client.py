import socket


def main():
    HOST = 'localhost'
    PORT = 11111

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            a = float(input("Введите длину основания (a): "))
            b = float(input("Введите длину второго основания (b): "))
            h = float(input("Введите высоту (h): "))

            request_data = f'{a},{b},{h}'
            s.sendall(request_data.encode('utf-8'))

            response = s.recv(1024).decode('utf-8')
            print(response)


if __name__ == '__main__':
    main()
