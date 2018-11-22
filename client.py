#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

host = "10.0.0.4"
porta = 23000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host,porta))

cliente.send("Tempartura")

resposta = cliente.recv(4096)

print resposta
