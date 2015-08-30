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
		answer = ''
		port.write('%s\n' % answer)
		port.flush()

WEST = 0
EAST = 1
NORTH = 2
SOUTH = 3

pos = [0, 0]
w   =  WEST
MAX_SIZE = 14
count = 0

dird = {0:"WEST", 1:"EAST", 2:"NORTH", 3:"SOUTH"}

def game1(line):
	if line == 'Nano$ show map':
		global lines
		global pos
		global w
		global MAX_SIZE
		global count
		global dird
		count = count + 1

		# here is map
		lines = lines[-3:]
		# for line in lines:
		# 	print line
		# write you rules to send [w] [a] [s] [d] here
		# 


		mymap = lines
		i = 0
		j = 0
		for i in range(3):
			try:
				j = mymap[i].index('O')
				break
			except ValueError:
				continue
		print "%d %d %d %d %s" %(pos[0], pos[1], i, j, dird[w])
		# write you rules to calculate answer here
		while True:
			if w is WEST:
				if pos[1] == 0 or mymap[i][j-1] == '+': # Wall Exist
					if pos[0] == MAX_SIZE or mymap[i + 1][j] == '+': # Wall
						w = SOUTH
						continue
					else:
						port.write('s\n')
						pos[0] = pos[0] + 1
						break
				else:
					port.write('a\n')
					pos[1] = pos[1] - 1
					w = NORTH
					break
			elif w is EAST:
				if pos[1] == MAX_SIZE or mymap[i][j+1] == '+': # Wall Exist
					if pos[0] == 0 or mymap[i - 1][j] == '+': # Wall
						w = NORTH
						continue
					else:
						port.write('w\n')
						pos[0] = pos[0] - 1
						break
				else:
					port.write('d\n')
					pos[1] = pos[1] + 1
					w = SOUTH
					break
			elif w is NORTH:
				if pos[0] == 0 or mymap[i - 1][j] == '+': # Wall Exist
					if pos[1] == 0 or mymap[i][j - 1] == '+': # Wall
						w = WEST
						continue
					else:
						port.write('a\n')
						pos[1] = pos[1] - 1
						break
				else:
					port.write('w\n')
					pos[0] = pos[0] - 1
					w = EAST
					break
			elif w is SOUTH:
				if pos[0] == MAX_SIZE or mymap[i + 1][j] == '+': # Wall Exist
					if pos[1] == MAX_SIZE or mymap[i][j + 1] == '+': # Wall
						w = EAST
						continue
					else:
						port.write('d\n')
						pos[1] = pos[1] + 1
						break
				else:
					port.write('s\n')
					pos[0] = pos[0] + 1
					w = WEST
					break
		port.flush()

	else:
		lines.append(line)



def game2(line):
	if line == 'Nano$ enter your answer:':
		global lines
		lines = lines[-1:]
		total = 0
	else:
		lines.append(line)

def main():
	# enter your choice here
	choice = '1'
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