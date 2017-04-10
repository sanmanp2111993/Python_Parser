import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as BS
import lxml.html as LH
import gzip
import zlib, base64
import shutil
import sys
import os

#######################################################
def datacompress(content):

	with gzip.open('file.txt.gz', 'wb') as f:
	    f.write(content)

	with open('file.txt.gz', 'rb') as f:
	    file_content = f.read()
 	return file_content

#######################################################
def datauncompress(compresseddata):
	with gzip.open('file1.txt.gz', 'wb') as f:
	    f.write(compresseddata)

	with gzip.open('file.txt.gz', 'rb') as f:
	    file_content1 = f.read()
	os.system('rm file1.txt.gz')
	return file_content1
########################################################
try:
	if sys.argv[2] == "gzip":
		file = open(sys.argv[1], 'r')
		filedata = file.readlines()
		endtag = "xyz"
		switch = 0

		bookstore = open('comprdata.xml','a')

		for data in filedata:
			if 'test="1"' in data :
				starttag = re.findall('<.*>',data)
				reftag = re.findall('/?\w+\s', data)
				newreftag = str(reftag[0])[0:len(reftag[0])-1]
				switch = 1
				bookstore.write(str(starttag[0]))
				endtag = '</'+(reftag[0])
				endtag = endtag[:len(endtag)-1] +">"

			if switch == 1:
				tempfile = open("temp.txt",'a+')
				tempfile.write(data)
				tempfile.close()
			if switch == 0:
				bookstore.write(data)
				bookstore.write("\n")
			if endtag in data:
				switch = 0

				file = open('temp.txt','r+')
				data1 = file.read()
				file.close()
				bookstore.write(datacompress(data1))
				bookstore.write(endtag)
				bookstore.write('\n')
		os.system('rm temp.txt')

	elif sys.argv[2] == "gunzip":
		file = open('comprdata.xml', 'r')
		filedata = file.readlines()
		endtag = "xyz"
		switch = 0
		bookstore = open('uncomprdata.xml','a')
		tempfile = open("temp1.txt",'a+')

		for data in filedata:
			if 'test="1"' in data :
				starttag = re.findall('<.*>',data)
				reftag = re.findall('/?\w+\s', data)
				newreftag = str(reftag[0])[0:len(reftag[0])-1]
				switch = 1
				endtag = '</'+(reftag[0])
				endtag = endtag[:len(endtag)-1] +">"
			if switch == 1:
				tempfile.write(data)
			if switch == 0:
				bookstore.write(data)
			if endtag in data:
				switch = 0

				file = open('temp1.txt','r+')
				uncompdata = datauncompress(file.read())
				bookstore.write(uncompdata)
		os.system('rm temp1.txt')
		os.system('curl -X POST -d comprdata.xml http://posttestserver.com/post.php')
	if sys.argv[2] == 'gunzip':
		os.system('rm file.txt.gz')
except:
	print '''\t\tInvlaid argument.
	\tPlease enter input command in the following manner:-
	\tpython parser.py (filname) gzip or
	\tpython parser.py (filename) gunzip.'''
