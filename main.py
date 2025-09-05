import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <-- Add this line

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(('', 3777))

broadcast_address = ('255.255.255.255', 3777)

message = b"Hello, World!"

s.sendto(message, broadcast_address)

print(f"Broadcast message '{message.decode()}' sent!")

# Close the socket
s.close()