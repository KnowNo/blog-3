import contextlib

@contextlib.contextmanager
def tag(name):
	print "<%s>" % name
	yield
	print "</%s>" % name


with tag('html'):						# before yield
	print "This is a html document"		# After yield
										# After exit scope




@contextlib.contextmanager
def closing(obj):
	try:
		yield obj
	finally:
		thing.close()
		
class Thing:
	def close(self):
		print "Thing.close()"


thing = Thing()
with closing(thing) as obj:
	print "Before close Thing"
