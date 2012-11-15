import unittest, glob, os
import pyless

###
'''
To launch unit test:
python -m unittest -v tests
'''
###

class TestCSS(unittest.TestCase):
	'''Iterate via test/css/ folder, seek for *.css files and parse them.
	There should be no parsing error.
	'''

	counter = 0

	def _do_css_test(self, fname):
		lexer, parser, result = pyless.parse(fname)
		if lexer.getNumberOfSyntaxErrors() > 0:
			self.fail("Lexer errors:\n" + '\n'.join(lexer.errormsgcache))
		if parser.getNumberOfSyntaxErrors() > 0:
			self.fail("Parser errors:\n" + '\n'.join(parser.errormsgcache))

		r = result.tree.toStringTree()
		self.assertIsNotNone(r, "Parsing silently failed!")

	def test_count(self):
		'Ensuring that there is correct number of CSS files to test parser.'
		self.assertEqual(self.counter, 27, "Number of *.css files to be tested is not correct (counter={0})".format(self.counter))


def testcss_generator(fname):
	def test(self):
		self._do_css_test(fname)
	return test

for f in glob.glob(os.path.join(os.path.dirname(__file__),'..','tests','css','*.css')):
	TestCSS.counter += 1
	test_name = 'test_css_{0:02d}_{1}'.format(TestCSS.counter, os.path.basename(f)[:-4].replace('-','_'))
	test = testcss_generator(f)
	test.func_doc = os.path.basename(f)
	setattr(TestCSS, test_name, test)

#
