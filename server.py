#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading

ip = "0.0.0.0"
porta = 23000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ip, porta)

server.listen(5)

print "Ouvindo em %s:%d" % (ip,porta)

def cliente(cliente_socket):
	resposta = cliente_socket.recv(1024)

	print "Resposta: %s" % resposta

	cliente_socket.send("70º")

	cliente_socket.close()

while True:

	client, addr = server.accept()

	print "Conexao recebida por: %s:%d" % (addr[0],addr[1])

	cliente = threading.Thread(target=cliente, args=(client,))

	cliente.start()
