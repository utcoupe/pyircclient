


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



