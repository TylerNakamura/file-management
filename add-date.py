import os
import platform
import argparse
import subprocess
import time
import datetime


def creation_date(path_to_file):
	last_modified = os.path.getmtime(path_to_file)
	"""
	Try to get the date that a file was created, falling back to when it was
	last modified if that isn't possible.
	See http://stackoverflow.com/a/39501288/1709587 for explanation.
	"""
	if platform.system() == 'Windows':
		ctime = os.path.getctime(path_to_file)
		if ctime < last_modified:
			return ctime
		else:
			return last_modified
	else:
		stat = os.stat(path_to_file)
		try:
			birthtime = stat.st_birthtime
			#print "comparing", birthtime, "and", last_modified
			if birthtime < last_modified:
				return datetime.datetime.utcfromtimestamp(birthtime).strftime("%Y-%m-%d")
			else:
				return datetime.datetime.utcfromtimestamp(last_modified).strftime("%Y-%m-%d")
		except AttributeError:
			# We're probably on Linux. No easy way to get creation dates here,
			# so we'll settle for when its content was last modified.
			print "exception caught, you are on Linux, right?"
			mtime = stat.st_mtime
			return datetime.datetime.utcfromtimestamp(mtime).strftime("%Y-%m-%d")

def files_in_dir(directory):
	ret_files = []
	for root, dirs, files in os.walk(directory):
		for i in files:
			ret_files.append(os.path.join(root, i))
	return ret_files

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("target", help="the directory to be renamed")
	parser.add_argument("-i", action="store_true", help="interactively rename files")
	args = parser.parse_args()
	for f in files_in_dir(args.target):
		newname = creation_date(f)+" "+os.path.basename(f)
		newpath = os.path.join(os.path.dirname(f),newname)
		if args.i:
			print "Would you like to rename", f, "to", newpath, "? y/n:"
			if (raw_input() == 'y'):
				os.rename(f, newpath)
		else:
			os.rename(f, newpath)

if __name__ == "__main__":
	main()
