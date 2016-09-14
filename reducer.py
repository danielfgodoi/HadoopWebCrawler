# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems
# File: reducer.py

import sys
import re
import os

def crawler(url):
	try:
		# URL
		print "========== URL ==========\n"
		print url
		os.system("wget -O data/index.html -q " + url)
		os.system("lynx -dump -assume_charset=utf8 -nolist -verbose data/index.html > data/index.html.txt")

	# Exception in case that could not download HTML
	except Exception, e:
		raise e
		print "Could not create dir and/or download file"

	# Parse HTML file to extract title
	with open("data/index.html", "r") as myfile:
		html = myfile.read().replace("\n", "")

	# Title
	print "\n========== TITLE ==========\n"
	regex = re.compile("<title>(.*?)</title>", re.IGNORECASE|re.DOTALL)
	try:
		title = regex.search(html).group(1)
	except Exception, e:
		title = "Could not get website title"
	del html
	print title

	# Body
	print "\n========== BODY ==========\n"
	with open("data/index.html.txt", "r") as myfile:
		body = myfile.read().replace("\n\n", "\n")
	print body, "========== END ==========\n"

	# Do the process recursively for each url found in HTML (lynx -dump -listonly)
	# os.system("lynx -dump -listonly -hiddenlinks=ignore data/index.html | grep -o "http:.*" | sort | uniq > data/urls.txt")

	del url
	del title
	del body

def main():
	current_url = None
	url = None

	# Create dir to save HTML and TXT files
	# print "Creating dir \"data\""
	os.system("mkdir -p data")

	# Read input from STDIN
	for line in sys.stdin:
		# Remove whitespaces
		url = line.strip()

		# In case we have duplicated URLs we skip in here
		if current_url != url:
			if current_url:
				crawler(current_url)
			current_url = url

	# do not forget to output the last url if needed!
	if current_url == url:
		# print '%s' % (current_url)
		crawler(current_url)

if __name__ == "__main__":
	main()
