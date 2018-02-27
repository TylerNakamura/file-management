#! /usr/bin/python

import tcnfilemanagement
import os
import argparse
import subprocess

# THIS IS BROKEN

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("target", help="the target directory")
	args = parser.parse_args()

	for f in tcnfilemanagement.files_in_dir(args.target):
		# if the file found is an avi file
		if f[len(f)-4:].lower() == ".avi":
			tcnfilemanagement.convertavitomp4(f)
			os.remove(f)

if __name__ == "__main__":
	main()
