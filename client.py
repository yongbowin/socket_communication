import socket

ip_port = ('127.0.0.1',9999)
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

while True:
    inp = input('Pls input: ').strip()
    print("===> ", inp, type(inp))
    if inp == 'exit':
        break
    # str to byte
    inp = inp.encode(encoding="utf-8")
    sk.sendto(inp,ip_port)

sk.close()
