# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems
# File: mapper.py

import sys

def main():
	# Read input from STDIN
	for url in sys.stdin:
		
		# Remove whitespaces
		url = url.strip()

		# Print the url to STDOUT
		# The output will be the input for reducer
		print '%s' % (url)

if __name__ == "__main__":
	main()
	