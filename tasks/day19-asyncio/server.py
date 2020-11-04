#!/usr/bin/env python

import socket
import os
import time

def start_tcp_server(ip, tcp_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("S. Creating socket success")

    s.bind((ip, tcp_port))
    print ("S. Binding on to port %d, Success" % (tcp_port))

    s.listen(5)
    print ("S. Waiting for connection from clients...");

    tot_conn_count = 0
    while(1):
        nfd, addr = s.accept()
        tot_conn_count += 1
        print ("\n\nS. Connection count ", tot_conn_count)
        print ("S. Got the connection request from ",  addr);
        if (os.fork() == 0):
            print('Connection address:', addr)
            while 1:
                data = nfd.recv(1024)
                print ("S. Received message from client...")
                print("\t\t", data)

                if not data: break

                print ("S. Seding reply to client as ...")
                data = data.decode()
                if(data.find("Booleon") >= 0):
                    data = data.upper()
                    nfd.send(data.encode())  # echo
                elif(data.find("One-line") >= 0):
                    for i in range(3):
                        data = data + data.upper() + " "
                    nfd.send(data.encode())  # echo
                elif(data.find("One-page") >= 0):
                    for i in range(10):
                        data = data + data.upper() + " "
                        time.sleep(1)
                    nfd.send(data.encode())  # echo
                else:
                    nfd.send("INVALID Question type")  # echo

            nfd.close()
            exit(1)
        else:
            nfd.close()

def main():
    ip = '' 
    tcp_port = 5005
    start_tcp_server(ip, tcp_port)

if (__name__ == "__main__"):
    main()
