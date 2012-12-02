from . import antlr3
from ._antlrwrap import lesscsslexer, lesscssparser

def parse(input):
	'''
	@param input: filename or file-like object with CSS/LESS to parse
	'''
	if hasattr(input, 'read'):
		char_stream = antlr3.ANTLRStringStream(input.read())
	else:
		char_stream = antlr3.ANTLRFileStream(input)
	lexer = lesscsslexer(char_stream)
	tokens = antlr3.CommonTokenStream(lexer)
	parser = lesscssparser(tokens)
	return lexer, parser, tokens, parser.styleSheet()
