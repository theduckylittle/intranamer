#!/usr/bin/env python

#
# Copyright (c) 2009-2012, Dan "Ducky" Little 
#
# Contact:
#  @theduckylittle
#  danlittle@yahoo.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import time
import urllib2

def clean_title(s):
	s = s.replace('&quot;','"')

	return s

if(__name__ == "__main__"):
	sources = {
		# imdb
	}

	t_v = time.localtime()
	h = {
		'month' : '%02d' % t_v.tm_mon,
		'year' :  t_v.tm_year % 100,
		'day' : '%02d' % t_v.tm_mday
	}
	

	imdb_urls = [
		'http://www.imdb.com/name/nm0%(month)s%(day)s%(year)s/',
		'http://www.imdb.com/name/nm0%(day)s%(year)s%(month)s/',
		'http://www.imdb.com/title/tt0%(month)s%(day)s%(year)s/',
		'http://www.imdb.com/title/tt0%(day)s%(month)s%(year)s/',
		'http://www.imdb.com/title/tt1%(month)s%(day)s%(year)s/',
		'http://www.imdb.com/title/tt1%(day)s%(month)s%(year)s/',
	]
	for url in imdb_urls:
		f = urllib2.urlopen(url % h)
		content = f.read()
		p1 = content.find('<title>')
		p2 = content.find(' - IMDb', p1)

		print 'IMDb: ', clean_title(content[p1+7:p2])

