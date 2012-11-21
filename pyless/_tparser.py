from . import antlr3
from .treelesscss import treelesscss as _treelesscss

#

class lesscsstwalker(_treelesscss):
	'''Tree parser'''

	EOLSEMI = ';'
	LISTCOMA = ','
	EOLLBRACKET = ' {'
	EOLRBRACKET = '}'


	def __init__(self, input, state=None, *args, **kwargs):
		super(lesscsstwalker, self).__init__(input, state, *args, **kwargs)
		self.indent_level = 0

	def output(self, codetext):
		print self.indent_level*'\t' + codetext

#

def twalk(pres, tokens):
	nodes = antlr3.tree.CommonTreeNodeStream(pres.tree)
	nodes.setTokenStream(tokens)
	walker = lesscsstwalker(nodes)
	return walker, walker.styleSheet()
