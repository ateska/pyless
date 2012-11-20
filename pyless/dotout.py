import os, cgi
from .lesscssParser import tokenNames

def save_result(parser_result, fname):
	'''Save parser result (tree) to .dot file - this can be then open by Graphviz and investigated.'''

	fout = open(fname, "w")
	fout.write('digraph "{0}" {{\nratio="fill";packMode="graph";\n'.format(os.path.basename(fname)[:-4].replace('-','_')))
	fout.write('node [style="filled",fontname="Arial"];\n')

	def twalker(t):
		tname = tokenNames[t.getType()]
		if tname == str(t):
			fout.write('"{0}" [shape=ellipse,label="{1}",fillcolor=paleturquoise];\n'.format(
				id(t),
				_escape_dot_label(t)
				)
			)
		else:
			fout.write('"{0}" [shape=record,label="{{{2}|{1}}}",fillcolor=palegreen];\n'.format(
				id(t),
				_escape_dot_label(t),
				_escape_dot_label(tname)
				)
			)

		if t.parent is not None:
			fout.write('"{0}" -> "{1}";\n'.format(id(t.parent), id(t)))

		for ch in t.children:
			twalker(ch)

	twalker(parser_result.tree)

	fout.write("}\n")


_label_repls = {'\n' : '\\n', '{' : '\{', '}': '\}'}
def _escape_dot_label(label):
	label = cgi.escape("{0}".format(label), True)
	return reduce(lambda a, kv: a.replace(*kv), _label_repls.iteritems(), label)
