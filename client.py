#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

host = raw_input("Digite o ip do servidor: ")
separa = host.split('\n')
host = separa[0]
print(host)
porta = 23000


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host,porta))

cliente.send("GET")

resposta = cliente.recv(4096)

print resposta
