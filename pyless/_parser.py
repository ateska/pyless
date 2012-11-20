from . import antlr3
from ._antlrwrap import lesscsslexer, lesscssparser

def parse(fname):
	char_stream = antlr3.ANTLRFileStream(fname)
	lexer = lesscsslexer(char_stream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = lesscssparser(tokens)
	return lexer, parser, tokens, parser.styleSheet()
