"""
Copyright (c) 2012, Thomas Recouvreux
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
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
	
