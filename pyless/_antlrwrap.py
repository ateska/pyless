from .lesscssLexer import lesscssLexer as _lesscssLexer
from .lesscssParser import lesscssParser as _lesscssParser

#

class lesscsslexer(_lesscssLexer):


	def __init__(self, input=None, state=None):
		self.errormsgcache = []
		_lesscssLexer.__init__(self, input, state)


	def emitErrorMessage(self, msg):
		self.errormsgcache.append(msg)

#

class lesscssparser(_lesscssParser):


	def __init__(self, input, state=None, *args, **kwargs):
		self.errormsgcache = []
		_lesscssParser.__init__(self, input, state, *args, **kwargs)


	def emitErrorMessage(self, msg):
		self.errormsgcache.append(msg)
