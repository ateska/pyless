from . import antlr3
from ._antlrwrap import wlclexer, wlcparser

def parse(fname):
	char_stream = antlr3.ANTLRFileStream(fname)
	lexer = wlclexer(char_stream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = wlcparser(tokens)
	return lexer, parser, parser.styleSheet()
