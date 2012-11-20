from . import antlr3
from .treelesscss import treelesscss as _treelesscss

#

class lesscsstwalker(_treelesscss):
	'''Tree parser'''


	def TP_charSet(self, t):
		print '@charset {0};'.format(t)


	def TP_imports(self, t):
		print '@import {0};'.format(t)


#

def twalk(pres, tokens):
	nodes = antlr3.tree.CommonTreeNodeStream(pres.tree)
	nodes.setTokenStream(tokens)
	walker = lesscsstwalker(nodes)
	return walker, walker.styleSheet()
