import os
import platform
import argparse
import subprocess
import time
import datetime


def creation_date(path_to_file):
	"""
	Try to get the date that a file was created, falling back to when it was
	last modified if that isn't possible.
	See http://stackoverflow.com/a/39501288/1709587 for explanation.
	"""
	if platform.system() == 'Windows':
		return os.path.getctime(path_to_file)
	else:
		stat = os.stat(path_to_file)
		try:
			return datetime.datetime.utcfromtimestamp(stat.st_birthtime).strftime("%Y-%m-%d")
		except AttributeError:
			# We're probably on Linux. No easy way to get creation dates here,
			# so we'll settle for when its content was last modified.
			return stat.st_mtime

def files_in_dir(directory):
	ret_files = []
	for root, dirs, files in os.walk(directory):
		for i in files:
			ret_files.append(os.path.join(root, i))
	return ret_files

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("target", help="the directory to be renamed")
	args = parser.parse_args()
	for f in files_in_dir(args.target):
		newname = creation_date(f)+"-"+os.path.basename(f)
		newpath = os.path.join(os.path.dirname(f),newname)
		print f
		print newpath
		os.rename(f, newpath)

if __name__ == "__main__":
	main()
