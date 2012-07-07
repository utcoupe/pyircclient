"""
Copyright (c) 2012, Thomas Recouvreux
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import threading
import subprocess
import time

from ..mypyirc import bridgebot
from ..mypyirc.botlauncher import BridgeBotLauncher




class StandartioBot(bridgebot.BridgeBot):
	def __init__(self, *, server_ip, server_port, nickname, channel, exec_name, exec_params, protocol_file, protocol_prefixe):
		super().__init__(server_ip=server_ip, server_port=server_port,
			nickname=nickname, channel=channel,
			protocol_file=protocol_file, protocol_prefixe=protocol_prefixe)
		self.exec_name = exec_name
		self.exec_params = exec_params
		self.process = None
		self.lock_connect = threading.Lock()
		self.connect_exec()
		

	def connect_exec(self):
		def f():
			while True:
				try:
					# kill de l'ancien process
					if self.process:
						try:
							self.process.terminate()
							time.sleep(1)
							if not self.process.poll():
								self.process.terminate()
						except Exception:
							self.process = None
					print("Subprocess : ",self.exec_name, self.exec_params)
					self.process = subprocess.Popen([self.exec_name]+self.exec_params, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
				except Exception as ex:
					time.sleep(1)
				else:
					print("connection ok")
					self.sendall("connection ok")
					break
		if self.lock_connect.acquire(False):
			t = threading.Thread(target=f)
			t.setDaemon(True)
			t.start()
			self.lock_connect.release()
			
	
	def write(self, msg):
		""" #écrit sur l'input standart """
		if msg:
			print("%s" % msg.strip())
			msg = bytes(msg.strip()+"\n","utf-8")
			try:
				self.process.stdin.write(msg)
				self.process.stdin.flush()
			except IOError:
				self.connect_exec()
				return 'IOError'

	def read(self):
		try:
			self.process.stdout.flush()
			m = str(self.process.stdout.readline(),"utf-8")
		except IOError:
			self.connect_exec()
			return 'IOError'
		else:
			return m

	def cmd__setexe(self, exe, args, *, id_msg=42, **kwargs):
		"""
		changer l'executable
		@param exe nom de l'executable
		@param args la liste des arguments, séparés par une virgule
		"""
		self.exec_name = exe
		self.exec_args = args[1:-1].split(',')
		self.connect_exec()



class StandartioBotLauncher(BridgeBotLauncher):
	def __init__(self, *, exec_name="./test.py", exec_params=[], **kwargs):
		super().__init__(bot_class=StandartioBot, **kwargs)
		self.parser.add_option("-e", "--exec-name",
							action="store", dest="exec_name", default=exec_name,
							help="nom de l'executable")
		self.parser.add_option("-p", "--exec-params",
							action="callback", callback=self.cb_params,
							dest="exec_params", default=exec_params,
							help="paramètres de l'executable séparés par ','")

	def cb_params(self, option, opt, value, parser):
		return value.split(',')


	
if __name__ == "__main__":
	launcher = StandartioBotLauncher()
	launcher.run()
	
