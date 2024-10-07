import socket  # Импортируем модуль socket для работы с сетевыми соединениями

# Запрашиваем у пользователя адрес сервера и номер порта
host = input("host:")  # Например, 'localhost' или '127.0.0.1'
port = int(input("port:"))

# Создаем TCP/IP сокет
# socket.AF_INET указывает, что используем IPv4
# socket.SOCK_STREAM указывает, что используем протокол TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем блокирующий режим сокета (по умолчанию блокирующий)
# В блокирующем режиме операции send() и recv() блокируют выполнение программы до завершения операции
# sock.setblocking(1)  # Эта строка необязательна и оставлена для информации

# Устанавливаем соединение с сервером по указанному адресу и порту
sock.connect((host, port))
print("Connected to server")  # пункт 4.i выполнен

# Основной цикл для отправки сообщений на сервер
while True:
    # Запрашиваем у пользователя сообщение для отправки на сервер
    msg = input("Your string (type 'exit' to quit):")
    # Отправляем сообщение серверу
    # Метод send() принимает данные типа bytes, поэтому преобразуем строку в байты методом encode()
    # По умолчанию используется кодировка UTF-8
    sock.send(msg.encode('utf-8'))
    print("Message sent to server")  # пункт 4.iii выполнен

    # Проверяем, отправил ли пользователь команду 'exit'
    if msg.lower() == 'exit':
        # Если отправлена команда 'exit', ожидаем ответ от сервера и затем завершаем цикл
        data = sock.recv(1024)  # Получаем данные от сервера (максимум 1024 байта)
        print("Message received from server")  # пункт 4.iv выполнен
        print(data.decode('utf-8'))  # Декодируем и выводим сообщение от сервера
        break  # Выходим из цикла и закрываем соединение
    else:
        # Если отправлено обычное сообщение, ожидаем ответ от сервера
        data = sock.recv(1024)
        print("Message received from server")  # пункт 4.iv выполнен
        # Декодируем и выводим ответ сервера
        print("Response from server:", data.decode('utf-8'))

# После выхода из цикла закрываем соединение с сервером
sock.close()
print("Connection closed to server")  # пункт 4.ii выполненs