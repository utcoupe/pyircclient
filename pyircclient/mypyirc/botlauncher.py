"""
Copyright (c) 2012, Thomas Recouvreux
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import optparse

from .mypyircbot import MyPyIrcBot
from .bridgebot import BridgeBot


class BotLauncher:
	"""
		Permet de lancer un bot en récupérant les paramètres passés au script
	"""
	def __init__(self, *, bot_class=MyPyIrcBot, server_ip="localhost", server_port=6667, nickname="pybot", channel="#test"):
		self.bot_class = bot_class
		
		usage = "usage: %prog [options]"
		self.parser = optparse.OptionParser(usage,version="%prog 0.0")
		self.parser.add_option("-S", "--server-ip",
							action="store", dest="server_ip", default=server_ip,
							help="ip irc server")
		self.parser.add_option("-P", "--server-port",
							action="store", dest="server_port", type="int", default=server_port,
							help="port irc server")
		self.parser.add_option("-n", "--nickname",
							action="store", dest="nickname", default=nickname,
							help="nickname on irc")
		self.parser.add_option("-c", "--channel",
							action="store", dest="channel", default=channel,
							help="channel on irc")
	
	def run(self, block=True):
		"""
			Créer un bot et le lancer
			@param {bool} block si False, le bot sera lancé dans un thread
			@return {Bot} le bot créé
		"""

		(options, _args) = self.parser.parse_args()

		d = {}
		for key in self.parser.defaults:
			d[key] = getattr(options, key)

		print(d)
		bot = self.bot_class(**d)

		if block:
			bot.start()
		else:
			t = threading.Thread(None, bot.start)
			t.setDaemon(True)
			t.start()

		return bot


class BridgeBotLauncher(BotLauncher):
	def __init__(self, *, bot_class=BridgeBot, protocol_file="protocol.h", protocol_prefixe="Q_", **kwargs):
		super().__init__(bot_class=bot_class, **kwargs)
		self.parser.add_option("-f", "--protocol-file",
							action="store", dest="protocol_file", default=protocol_file,
							help="protocol file")
		self.parser.add_option("-x", "--protocol-prefixe",
							action="store", dest="protocol_prefixe", default=protocol_prefixe,
							help="protocol prefixe")



