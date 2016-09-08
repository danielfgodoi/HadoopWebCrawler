# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems

from subprocess import call
import sys
import re
import os
import re

if __name__ == "__main__":
	# Get file name	
	try:
		fileName = sys.argv[1]
	except:
		print "Missing file name"
		sys.exit(0)

	# Read file
	try:
		with open(fileName) as f:
			links = f.readlines()
		links = [line.rstrip('\n') for line in links]
		
		# Create dir to download files
		try:
			print "Creating dir data/\n"
			os.system("mkdir -p data")
			# call(["mkdir", "-p", "data"])
		except Exception, e:
			raise e
			sys.exit(0)

		# Download files
		# print "Downloading links: ", links
		for link in links:
			try:
				# Download url index HTML
				print "Dowloading HTML content"
				os.system("wget -O data/index.html -q " + link)

			# Exception in case that could not download HTML
			except Exception, e:
				raise e
				print "Could not create dir and/or download file"

			# Parse HTML file to extract title
			with open('data/index.html', 'r') as myfile:
				html = myfile.read().replace('\n', '')
			
			# Title
			regex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)
			title = regex.search(html).group(1)
			print title + "\n"

			# 
			regex = re.compile('<body(.*?)</body>', re.IGNORECASE|re.DOTALL)
			body = regex.search(html).group(1)
			print body + "\n"

	# Éxception in case that could not open file
	except Exception, e:
		raise e
		sys.exit(0)
