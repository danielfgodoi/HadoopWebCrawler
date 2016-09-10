# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems

from subprocess import call
import sys
import re
import os

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
			print "\n========== STARTING ==========\n"
			print "Creating dir \"data\""
			os.system("mkdir -p data")
		except Exception, e:
			raise e
			sys.exit(0)

		# Download files
		# print "Downloading links: ", links
		for link in links:
			try:
				# Download url index HTML
				print "\n========== URL ==========\n"
				print "Dowloading url content from \"" + link + "\""
				os.system("wget -O data/index.html -q " + link)
				os.system("lynx -dump data/index.html -nolist > data/index.html.txt")

			# Exception in case that could not download HTML
			except Exception, e:
				raise e
				print "Could not create dir and/or download file"

			# Parse HTML file to extract title
			with open('data/index.html', 'r') as myfile:
				html = myfile.read().replace('\n', '')
			
			# Title
			print "\n========== TITLE ==========\n"
			regex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)
			title = regex.search(html).group(1)
			print title

			# Body with tags
			regex = re.compile('<body(.*?)</body>', re.IGNORECASE|re.DOTALL)
			bodyWithTags = regex.search(html).group(1)

			# Also working
			# regex = re.compile('<.*?>')
			# body = re.sub(regex,'', bodyWithTags)

			# Body without tags
			print "\n========== BODY ==========\n"
			body = re.sub('<.*?>', '', bodyWithTags)
			body = ' '.join(body.split())
			print body

	# Éxception in case that could not open file
	except Exception, e:
		raise e
		sys.exit(0)
