import unittest, os
import pyless
from ._testbed import *

###
'''
To launch unit test:
python -m unittest -v tests
'''
###

class TestF01CSS(FileBasedParserTest):
	'''Iterate via test/css/ folder, seek for *.css files and parse them.
	There should be no parsing error.
	'''

	counter = 0
	name = 'css'

	def test_count(self):
		'Ensuring that there is correct number of CSS files to test parser.'
		self.assertEqual(self.counter, 8, "Number of *.css files to be tested is not correct (counter={0})".format(self.counter))

TestF01CSS.AddTestDirGlob(os.path.join(os.path.dirname(__file__),'..','tests','css','*.css'))

#

class TestF02LessCSS(FileBasedParserTest):
	'''Iterate via test/css/ folder, seek for *.css files and parse them.
	There should be no parsing error.
	'''

	counter = 0
	name = 'lesscss'

	def test_count(self):
		'Ensuring that there is correct number of CSS files to test parser.'
		self.assertEqual(self.counter, 29, "Number of *.css files to be tested is not correct (counter={0})".format(self.counter))

TestF02LessCSS.AddTestDirGlob(os.path.join(os.path.dirname(__file__),'..','tests','less-css','*.css'))

#

class TestF03BootstrapCSS(FileBasedParserTest):
	'''Iterate via test/bootstrap/ folder, seek for *.css files and parse them.
	There should be no parsing error.
	'''

	counter = 0
	name = 'bootstrap'

	def test_count(self):
		'Ensuring that there is correct number of CSS files to test parser.'
		self.assertEqual(self.counter, 4, "Number of *.css files to be tested is not correct (counter={0})".format(self.counter))

TestF03BootstrapCSS.AddTestDirGlob(os.path.join(os.path.dirname(__file__),'..','tests','bootstrap','*.css'))

#
