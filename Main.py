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
		print "Missing file name!"
		sys.exit(0)

	# Read file
	try:
		with open(fileName) as f:
			links = f.readlines()
		links = [line.rstrip('\n') for line in links]
		
		# Download files
		# print "Downloading links: ", links
		for link in links:
			try:
				print ""
				# print "Downloading urls..."
				# Create dir to download file
				# d = link.replace("https://", "")
				# call(["mkdir", "-p", d])
				# call(["mkdir", "-p", "data"])
				
				# Dá pra parsear o arquivo para renomeá-lo (ruim)
				# linkName = link.replace("//", "")
				# print linkName + "\n"

				# call(["wget", link])
				# call(["wget", "-qO-", "http://globoesporte.globo.com/futebol/futebol-internacional/jogo/06-09-2016/suica-portugal/", "|", "grep", "-iPo", "(?<=<title>)(.*)(?=</title>)"])

				cmd = "wget -qO- " + link + " | perl -l -0777 -ne 'print $1 if /<title.*?>\s*(.*?)\s*<\/title/si'"
				# linkName = os.system(cmd)

				p1 = subprocess.Popen(["wget", "-qO-", link], stdout=subprocess.PIPE)
				p2 = subprocess.Popen(["perl", "-l", "-0777", "-ne", "'print $1 if /<title.*?>\s*(.*?)\s*<\/title/si'"], stdin=p1.stdout, stdout=subprocess.PIPE)
				p2.communicate()

			# Exception in case that could not download file
			except:
				print "Could not create dir and/or download file!"

		# Write the parser here

	# Éxception in case that could not open file
	except:
		print "Could not open file", "\""+fileName+"\"!"
