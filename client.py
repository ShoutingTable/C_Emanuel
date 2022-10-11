import socket
import argparse


client_parse = argparse.ArgumentParser(description='command line parser')

client_parse.add_argument('-l', type=str,
                    help='Log File Location')

client_parse.add_argument('-p', type=int, nargs='?',
                    help='Port')

client_parse.add_argument('-s', type=str,
                    help='Server ID ')

client_parse.add_argument('client', type=str,
                    help='Server ID ')

client_parse.add_argument('$', type=str,
                    help='Server ID ')

cli_args = client_parse.parse_args()


Host= cli_args.s 
Port= cli_args.p
Log_Location= cli_args.l
print("The values are:")


print(f"IP Address: {Host}")
print(f"Port #: {Port}")
print(f"Log File Location: {Log_Location}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as a:
    a.connect((Host, Port))
    line = input("Enter a message: ")
    a.send(line.encode())
    data = a.recv(1024)
    print("Message from server: ", data.decode())
    a.close()

print(f"Message received: {data}")
    