#! /usr/bin/python

import os
import argparse
import subprocess

# INPUT - full path of target avi
# This will fuck up if there is .avi in the path and NOT the basename
def convertavitomp4(f):
	subprocess.check_call(["avconv", "-i", f, "-c:v", "libx264", "-preset", "veryslow", "-c:a", "copy", f.replace(".avi", ".mp4")])

# returns a list of the recursive files in the input directory
def files_in_dir(directory):
	ret_files = []
	for root, dirs, files in os.walk(directory):
		for i in files:
			ret_files.append(os.path.join(root, i))
	print ret_files
	return ret_files

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("target", help="the target directory")
	parser.add_argument("-d", "--delete", help="delete the files after conversion", action="store_true", default=False)
	args = parser.parse_args()

	for f in files_in_dir(args.target):
		# if the file found is an avi file
		if f[len(f)-4:].lower() == ".avi":
			convertavitomp4(f)
			# If the delete flag has been specified
			if args.delete:
				print "deleting", f
				subprocess.check_call(["rm", f])
			else:
				print "delete option was not specified, so", f, "will not be deleted..."

if __name__ == "__main__":
	main()
