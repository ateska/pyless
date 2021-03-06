import unittest, glob, os, StringIO
import pyless
from pyless.antlr3 import tree
from pyless import dotout
##

def _fbtgen(fname):
	def test(self):
		self._do_file_test(fname)
	return test


class FileBasedParserTest(unittest.TestCase):

	counter = None # Override this !
	name = None  # Override this !

	def _do_file_test(self, fname):
		# Parse input file
		lexer, parser, tokens, presult = pyless.parse(fname)
		if lexer.getNumberOfSyntaxErrors() > 0:
			self.fail("Lexer errors:\n" + '\n'.join(lexer.errormsgcache))
		if parser.getNumberOfSyntaxErrors() > 0:
			self.fail("Parser errors:\n" + '\n'.join(parser.errormsgcache))

		r = presult.tree.toStringTree()
		self.assertIsNotNone(r, "Parsing silently failed!")

		# Save graph to dot
		dotout.save_result(presult, fname+".dot")

		# Tree walk
		output = StringIO.StringIO()
		twalker, tresult = pyless.twalk(presult, tokens, output=output)
		if twalker.getNumberOfSyntaxErrors() > 0:
			self.fail("Tree walker errors:\n" + '\n'.join(twalker.errormsgcache))

		output.seek(0)
		output2nd = self._reparse(output)

		# Compare outputs - must be the same
		output.seek(0)
		self.assertEqual(output.getvalue(), output2nd.getvalue())


	def _reparse(self, output):
		# Reparse output CSS again
		lexer, parser, tokens, presult = pyless.parse(output)
		if lexer.getNumberOfSyntaxErrors() > 0:
			self.fail("Lexer (reparse) errors:\n" + '\n'.join(lexer.errormsgcache))
		if parser.getNumberOfSyntaxErrors() > 0:
			self.fail("Parser (reparse) errors:\n" + '\n'.join(parser.errormsgcache))

		r = presult.tree.toStringTree()
		self.assertIsNotNone(r, "Parsing (reparse) silently failed!")

		# Tree walk
		output = StringIO.StringIO()
		twalker, tresult = pyless.twalk(presult, tokens, output=output)
		if twalker.getNumberOfSyntaxErrors() > 0:
			self.fail("Tree walker errors:\n" + '\n'.join(twalker.errormsgcache))

		output.seek(0)
		return output


	@classmethod
	def AddTestDirGlob(cls, dglob):

		for f in glob.glob(dglob):
			cls.counter += 1
			test_name = 'test_{name}_{counter:02d}_{fnamebase}'.format(name=cls.name,counter=cls.counter, fnamebase=os.path.basename(f)[:-4].replace('-','_'))
			test = _fbtgen(f)
			test.func_doc = os.path.basename(f)
			setattr(cls, test_name, test)
