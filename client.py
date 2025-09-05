import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 3777))

print("Listening for broadcast messages...")

# s.recvfrom(1024)

data, addr = s.recvfrom(1024)

print(f"Received message: {data.decode()} from {addr}")

# 5. Close the socket
s.close()