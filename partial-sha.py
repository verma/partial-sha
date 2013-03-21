# partial sha
#

import getopt
import os
import hashlib

class PartialSHA(object):
	def __init__(self, filename, **options):
		self.filename, self.options = filename, self._defaults(options)

	def _defaults(self, options):
		opts = {
			"startOffset": options.get("startOffset") if options.get("startOffset") else "0",
			"endOffset": options.get("endOffset") if options.get("endOffset") else "-1"
		}

		return opts;

	def hexdigest(self):
		s = os.stat(self.filename)
		filesize = s.st_size;

		def parseOffset(o):
			if o == "-1":
				return filesize
			if o.endswith('%'):
				return int(round(filesize * float(o[:-1]) / 100.0))
			return int(o)

		start, end = parseOffset(self.options['startOffset']), \
				parseOffset(self.options['endOffset'])
		if end < start:
			raise Exception('Start should be before the end')

		if start > filesize:
			raise Exception('Start is too big (larger than file size)')
		if end > filesize:
			raise Exception('End is too big (larger than file size)')

		offset, target = 0, end - start
		h = hashlib.sha1()
		with open(self.filename, "rb") as f:
			f.seek(start)
			while offset < target:
				b = f.read(min(target - offset, 2^24))
				offset += len(b)

				h.update(b)
		return h.hexdigest()

if __name__ == '__main__':
	import sys
	optlist, args = getopt.getopt(sys.argv[1:], "s:e:")

	if not args:
		print 'No file specified'
		sys.exit(1)

	d = dict(optlist)
	print PartialSHA(args[0], startOffset=d.get('-s'), endOffset=d.get('-e')).hexdigest()
	

