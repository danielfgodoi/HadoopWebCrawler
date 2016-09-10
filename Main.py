# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems

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
			urls = f.readlines()
		urls = [line.rstrip("\n") for line in urls]
		
		# Create dir to download files
		try:
			# print "\n========== STARTING ==========\n"
			# print "Creating dir \"data\""
			os.system("mkdir -p data")
		except Exception, e:
			raise e
			sys.exit(0)

		# Download files and parse the strings to get title and body
		for url in urls:
			try:
				# Download url index HTML
				# print "\n========== URL ==========\n"
				# print "Dowloading url content from \"" + url + "\""
				os.system("wget -O data/index.html -q " + url)
				os.system("lynx -dump data/index.html -nolist -verbose > data/index.html.txt")

			# Exception in case that could not download HTML
			except Exception, e:
				raise e
				print "Could not create dir and/or download file"

			# Parse HTML file to extract title
			with open("data/index.html", "r") as myfile:
				html = myfile.read().replace("\n", "")

			# Title
			# print "\n========== TITLE ==========\n"
			regex = re.compile("<title>(.*?)</title>", re.IGNORECASE|re.DOTALL)
			title = regex.search(html).group(1)
			del html
			# print title

			# Body
			# print "\n========== BODY ==========\n"
			with open("data/index.html.txt", "r") as myfile:
				body = myfile.read().replace("\n\n", "\n")
			# print body

			# Add to database

			# Do the process recursively for each url found in HTML (lynx -dump -listonly)

			del url
			del title
			del body

	# Éxception in case that could not open file
	except Exception, e:
		raise e
		sys.exit(0)
