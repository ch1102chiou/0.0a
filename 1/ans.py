#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import serial
import time

port = None

lines = []

def game0(line):
	if line == 'Nano$ enter your answer:':
		# enter you answer here
		answer = 'HITCONNANOGAMEMORSE'
		port.write('%s\n' % answer)
		port.flush()

def game1(line):
	if line == 'Nano$ show map':
		global lines
		# here is map
		lines = lines[-3:]
		# for line in lines:
		# 	print line
		# write you rules to send [w] [a] [s] [d] here

		port.write('d\n')
		port.flush()
	else:
		lines.append(line)

def game2(line):
	if line == 'Nano$ enter your answer:':
		global lines
		lines = lines[-1:]
		total = 0
		# write you rules to calculate answer here

		port.write('%d\n' % total)
		port.flush()
	else:
		lines.append(line)

def main():
	# enter your choice here
	choice = '0'
	while True:
		line = port.readline()[:-1]
		print line
		if line == 'Nano$ enter your choice:':
			port.write('%s\n' % choice)
			port.flush()
		if line == 'Nano$ finish':
			port.close()
			break
		if choice == '0':
			game0(line)
		if choice == '1':
			game1(line)
		if choice == '2':
			game2(line)
		if choice == '3':
			game3(line)

if __name__ == '__main__':
	port = serial.Serial(port="/dev/ttyUSB0", baudrate=57600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	port.close()
	port = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	if port.isOpen():
		print "This serial is open"
	main()
