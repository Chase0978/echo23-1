import socket  # Импортируем модуль socket для работы с сетевыми соединениями
from time import sleep  # Импортируем функцию sleep для возможной задержки (хотя она не используется в данном коде)

# Запрашиваем у пользователя адрес сервера и номер порта и преобразуем последний в целое число
host=input("host:")
port = int(input("port:"))

# Создаем новый сокет
sock = socket.socket()

# Устанавливаем режим блокирующего ввода/вывода (по умолчанию и так блокирующий, эта строка избыточна)
sock.setblocking(1)

# Устанавливаем соединение с сервером на localhost (127.0.0.1) и указанном порту
sock.connect((host, port))
print("Connected to server") # пункт 4.i выполнен

# Запрашиваем у пользователя строку для отправки
msg = input("Your string:")
# Закомментированная альтернатива - отправка фиксированной строки "Hi!"
#msg = "Hi!"

# Отправляем сообщение серверу, предварительно закодировав его в байты
sock.send(msg.encode())
print("Message sent to server") # пункт 4.iii выполнен

# Получаем ответ от сервера (не более 1024 байт)
data = sock.recv(1024)
print("Message received from server") # пункт 4.iv выполнен

# Закрываем соединение с сервером
sock.close()
print("Connection closed to server") # пункт 4.ii выполнен

# Выводим декодированный ответ от сервера
print(data.decode())