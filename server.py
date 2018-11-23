#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

print("Digite uma opcao de servidor:")
print("1 - Temperatura")
print("2 - Umidade")
print("3 - Deteccao Movimento")
type_server = int(input("Digite a opcao: "))#1,2,3 Temperatuta, Umidade, Deteccao_Movimento

ip = "0.0.0.0"
porta = 23000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((ip, porta))

server.listen(2)

while True:
	print('\n\n')
	print "Ouvindo em %s:%d" % (ip,porta)
	client, addr = server.accept()

	print "Conexao recebida por: %s:%d" % (addr[0],addr[1])

	while True:
		data = client.recv(1024)
		if not data: break
		if type_server == 1:
			client.send(b'[*]Temperatura: 60º')
		elif type_server == 2:
			client.send(b'[*]Umidade: 38%')
		else:
			client.send(b'[*]Dec_Movimento: Sem Movimentacao no local!')
	client.close()
