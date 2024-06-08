#!/usr/bin/python3
import serial
import sys

ser = serial.Serial()
ser.baudarte = 115200
ser.port = '/dev/ttyUSB1'
ser.open()

if len(sys.argv) > 1:
	request = sys.argv[1].encode()
	request += b'\r'
	ser.write(request)
	print(request)
else:
	print("write AT in port")
	ser.write(b'AT\r')

answer = ser.read()
while not 'OK\r' in answer.decode():
	answer += ser.read()
	if 'ERROR' in answer.decode():
		break
	elif len(answer.decode()) > 100:
		break

print(answer)

ser.close()