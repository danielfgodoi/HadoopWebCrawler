#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Authors: Daniel Godoi and Lucas Arakaki
# Subject: Distributed Systems
# File: getURLs.py

# Note: This script only works on servers with LYNX installed

import sys
import os

def main():
	links = []
	os.system("mkdir -p data")
	os.system("rm data/urls.txt")
	for line in sys.stdin:
		url = line.strip()
		os.system("echo " + url + " >> data/urls.txt")
		os.system("lynx -dump -listonly -hiddenlinks=ignore " + url + " | grep -o \"http:.*\" | sort | uniq >> data/urls.txt")

if __name__ == "__main__":
	main()