
import serial
import sys
import time
#import logger

class IOPort:	
	ser = None
	port = None
	baudrate = None
	logger = None
	def __init__(self, port,  baudrate):
		self.ser = serial.Serial()
		self.baudrate = baudrate
		self.port = port
		self.ser.baudrate = baudrate
		self.ser.port = port		
		#self.logger = Logger()
		#self.logger.debug("[IOPort] oppened port [{}],  with baudrate [{}]", port, baudrate)	

	def write(self, string):
		if self.ser.is_open:
			self.ser.write(string)
		else:
			try:
				self.ser.open()
				self.ser.write(string)
			finally:
				self.ser.close

	def read(self, max_read_time = None):
		if self.ser.is_open:					
			answer = self.ser.read()
		else:
			try:
				self.ser.open()
				answer = self.ser.read()
			finally:
				self.ser.close()

		if not max_read_time:
			max_read_time = 5

		timing = time.time()
		while not 'OK\r' in answer.decode():
			if self.ser.is_open:					
				answer += self.ser.read()
			else:
				try:
					self.ser.open()
					answer += self.ser.read()
				finally:
					self.ser.close()
			
			if 'ERROR' in answer.decode():
				break
			elif 'CONNECT' in answer.decode():
				break
			elif len(answer.decode()) > 100:
				break
			elif time.time() - timing > max_read_time:
				break
		return answer
	
	def open(self):
		if not self.ser.is_open:
			self.ser.open()

	def close(self):
		if self.ser.is_open:
			self.ser.close()