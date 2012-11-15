from .lesscssLexer import lesscssLexer
from .lesscssParser import lesscssParser

#

class wlclexer(lesscssLexer):


	def __init__(self, input=None, state=None):
		self.errormsgcache = []
		lesscssLexer.__init__(self, input, state)


	def emitErrorMessage(self, msg):
		self.errormsgcache.append(msg)

#

class wlcparser(lesscssParser):


	def __init__(self, input, state=None, *args, **kwargs):
		self.errormsgcache = []
		lesscssParser.__init__(self, input, state, *args, **kwargs)


	def emitErrorMessage(self, msg):
		self.errormsgcache.append(msg)

