import unittest, glob, os, cgi
import pyless
from pyless.antlr3 import tree
from pyless.lesscssParser import tokenNames

##

def _fbtgen(fname):
	def test(self):
		self._do_file_test(fname)
	return test


class FileBasedParserTest(unittest.TestCase):

	counter = None # Override this !
	name = None  # Override this !

	def _do_file_test(self, fname):
		lexer, parser, result = pyless.parse(fname)
		if lexer.getNumberOfSyntaxErrors() > 0:
			self.fail("Lexer errors:\n" + '\n'.join(lexer.errormsgcache))
		if parser.getNumberOfSyntaxErrors() > 0:
			self.fail("Parser errors:\n" + '\n'.join(parser.errormsgcache))

		r = result.tree.toStringTree()
		self.assertIsNotNone(r, "Parsing silently failed!")

		###

		fout = open(fname+'.dot', "w")
		fout.write('digraph {0} {{\nratio = fill;packMode=graph;\n'.format(os.path.basename(fname)[:-4].replace('-','_')))
		fout.write('node [style="filled",fontname=Arial];\n')
		def twalker(t):
			tname = tokenNames[t.getType()]
			if tname == str(t):
				fout.write('"{0}" [shape=ellipse,label="{1}",fillcolor=paleturquoise];\n'.format(
					id(t),
					self._escape_dot_label(t)
					)
				)
			else:
				fout.write('"{0}" [shape=record,label="{{{2}|{1}}}",fillcolor=palegreen];\n'.format(
					id(t),
					self._escape_dot_label(t),
					self._escape_dot_label(tname)
					)
				)

			if t.parent is not None:
				fout.write('"{0}" -> "{1}";\n'.format(id(t.parent), id(t)))

			for ch in t.children:
				twalker(ch)

		twalker(result.tree)

		fout.write("}\n")
	
	
	_label_repls = {'\n' : '\\n', '{' : '\{', '}': '\}'}
	@classmethod
	def _escape_dot_label(cls, label):
		label = cgi.escape("{0}".format(label), True)
		return reduce(lambda a, kv: a.replace(*kv), cls._label_repls.iteritems(), label)


	@classmethod
	def AddTestDirGlob(cls, dglob):

		for f in glob.glob(dglob):
			cls.counter += 1
			test_name = 'test_{name}_{counter:02d}_{fnamebase}'.format(name=cls.name,counter=cls.counter, fnamebase=os.path.basename(f)[:-4].replace('-','_'))
			test = _fbtgen(f)
			test.func_doc = os.path.basename(f)
			setattr(cls, test_name, test)
