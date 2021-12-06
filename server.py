import socket

"""
-----------Socket accept 2 argument--------------- 
1. type of network i.e, ip v4 or ip v6 address
2. type of network TCP or UDP, by default is TCP 
"""
s = socket.socket()

print("Socket Created")

# Assign a ip address and a port number to this server and bind together.
# port number having Range Between  0 -> 65535
s.bind(('localhost', 9999))

# It listen only 3 Client Connection
s.listen(3)
print("Waiting for the connection")

while True:
    c, add = s.accept()
    """
    Accept connection form client & it gives 2 thing
    1st client socket and client address
    add contain 2 thing 1st is ip address of client and port number
    """

    print("Connected with ", add)

    name = c.recv(1024).decode()

    print("Connected with ", add, name)


    # Send From Server to Client
    c.send(bytes('Data From Server', 'utf-8'))

    c.close()
    # Close all resources





