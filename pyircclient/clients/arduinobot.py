import sys
import threading
import serial

from ..mypyirc import BridgeBot
from ..mypyirc.ircdefine import *
from ..mypyirc.botlauncher import BridgeBotLauncher



class ArduinoBot(BridgeBot):
	def __init__(self, *, server_ip, server_port, nickname, channel, serial_port, serial_baudrate, protocol_file, protocol_prefixe):
		BridgeBot.__init__(self, server_ip=server_ip, server_port=server_port,
			nickname=nickname, channel=channel,
			protocol_file=protocol_file, protocol_prefixe=protocol_prefixe)
		
		self.serial = None
		try:
			self.serial = serial.Serial(serial_port, serial_baudrate, timeout=1, writeTimeout=1)
		except serial.SerialException as ex:
			print("Erreur lors de l'ouverture du port série",ex)
			sys.exit(1)
		print("OK")
		

	
	def write(self, msg):
		""" écrit sur le port série """
		if msg:
			print("%s" % msg.strip())
			msg = bytes(msg.strip()+"\n","utf-8")
			self.serial.write(msg)

	def read(self):
		return str(self.serial.readline(),"utf-8")


class ArduinoBotLauncher(BridgeBotLauncher):
	def __init__(self, *, serial_port="/dev/ttyACM0", serial_baudrate=115200, **kwargs):
		super().__init__(bot_class=ArduinoBot, **kwargs)
		self.parser.add_option("-s", "--serial-port",
							action="store", dest="serial_port", default=serial_port,
							help="serial port")
		self.parser.add_option("-p", "--serial-baudrate",
							action="store", dest="serial_baudrate", default=serial_baudrate,
							help="serial baudrate")


	
if __name__ == "__main__":
	launcher = ArduinoBotLauncher()
	launcher.run()
	
