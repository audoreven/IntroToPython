import socket

url = input("Enter URL: ")
# url = "http://data.pr4e.org/romeo.txt"
max_chars = 3000

try:
    words = url.split('/')
    host = words[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysocket.send(cmd)
except IndexError:
    print("Invalid URL.")
    exit(-1)
except OSError:
    print("Invalid URL.")
    exit(-1)
except socket.gaierror:
    print("URL does not exit.")
    exit(-2)

total = 0
while True:
    data = mysocket.recv(128)
    if len(data) < 1:
        break
    if total + len(data) < max_chars:
        print(data.decode(), end='')
    elif total + len(data) > max_chars > total:
        print(data.decode()[max_chars - total], end='')
        total = max_chars
    total += len(data)

print("\n\nTotal characters:", total)

total = 0

mysocket.close()
