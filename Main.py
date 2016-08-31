# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems

import sys
from subprocess import call

if __name__ == "__main__":
	# Get file name
	fileName = sys.argv[1]
	
	# Read file
	try:
		with open(fileName) as f:
			links = f.readlines()
		links = [line.rstrip('\n') for line in links]
		
		# Download files
		# print "Downloading links: ", links
		for link in links:
			try:
				# Create dir to download file
				d = link.replace("https://", "")
				call(["mkdir", "-p", d])
				call(["wget", "-nc", "-P", d, link])

			# Exception in case that could not download file
			except:
				print "Could not create dir and download file. Does user have needed permission?"

		# Write the parser here

	# Éxception in case that could not open file
	except:
		print "Could not open file", fileName+".", "The file doesn't exist or is being used by another program!"
