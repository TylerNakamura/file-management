import os
import platform
import argparse
import subprocess
import time
import datetime

"""
	Try to get the date that a file was created, falling back to when it was
	last modified if that isn't possible.
	See http://stackoverflow.com/a/39501288/1709587 for explanation.
"""
def creation_date(path_to_file):
	last_modified = os.path.getmtime(path_to_file)

	# if the system running the script is a Windows system
	if platform.system() == 'Windows':
		ctime = os.path.getctime(path_to_file)
		if ctime < last_modified:
			return datetime.datetime.utcfromtimestamp(ctime).strftime("%Y-%m-%d") + " "
		else:
			return datetime.datetime.utcfromtimestamp(last_modified).strftime("%Y-%m-%d") + " "
	# if the system running the script is NOT a Windows system
	else:
		stat = os.stat(path_to_file)
		try:
			birthtime = stat.st_birthtime
			# We are really looking for the earliest known date here.
			# This happens to be a personal preference as I think it is the best known guess of when the file was created
			if birthtime < last_modified:
				return datetime.datetime.utcfromtimestamp(birthtime).strftime("%Y-%m-%d")
			else:
				return datetime.datetime.utcfromtimestamp(last_modified).strftime("%Y-%m-%d")
		# We're probably on Linux. No easy way to get creation dates here,
		# so we'll settle for when its content was last modified.
		except AttributeError:
			mtime = stat.st_mtime
			return datetime.datetime.utcfromtimestamp(mtime).strftime("%Y-%m-%d")
'''
	returns a list of files (full path) within the directory
	note that this method recurses
'''
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
	parser.add_argument("-c", help="Set a custom date")
	args = parser.parse_args()

	# for every file in our target directory
	for f in files_in_dir(args.target):
		# if the custom dating argument is set and we want to specify a custom date
		if args.c:
			newname = args.c + " " + os.path.basename(f)
		# otherwise, let's make our best guess and use the earliest of the creation or modification date
		else:
			newname = str(creation_date(f))+" "+os.path.basename(f)

		# create the new full path with the new name that was just created
		newpath = os.path.join(os.path.dirname(f),newname)
	
		# if interactive mode is being used, ask the user if they would like to proceed with the action
		if args.i:
			print "Would you like to rename", f, "to", newpath, "? y/n:"
			if (raw_input() == 'y'):
				os.rename(f, newpath)
		# otherwise, just pull the trigger
		else:
			os.rename(f, newpath)

if __name__ == "__main__":
	main()
