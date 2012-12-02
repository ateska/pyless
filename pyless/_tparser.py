import sys
from . import antlr3
from .treelesscss import treelesscss as _treelesscss

#

class lesscsstwalker(_treelesscss):
	'''Tree walker/parser'''

	EOLSEMI = ';'
	LISTCOMA = ','
	EOLLBRACKET = ' {'
	EOLRBRACKET = '}'


	def __init__(self, input, state=None, output=sys.stdout, *args, **kwargs):
		super(lesscsstwalker, self).__init__(input, state, *args, **kwargs)
		self.indent_level = 0
		self.output = output
		self.errormsgcache = []

	def writeln(self, codetext):
		self.output.write(self.indent_level*'\t' + codetext + '\n')


	def emitErrorMessage(self, msg):
		self.errormsgcache.append(msg)

#

def twalk(pres, tokens, output=sys.stdout):
	nodes = antlr3.tree.CommonTreeNodeStream(pres.tree)
	nodes.setTokenStream(tokens)
	walker = lesscsstwalker(nodes,output=output)
	return walker, walker.styleSheet()
