#!/usr/bin/python


'''
    takes a list of string files and renames them properly
    rules:
        all lowercase
        replaces spaces with dashes
'''


def proper_name(file_name):
    file_name = file_name.lower()
    file_name = file_name.replace(' ', '-')
    return file_name


'''
    returns the full file path of all the files in input directory
'''


def files_in_dir(directory):
    import os
    ret_files = []
    for root, dirs, files in os.walk(directory):
        for i in files:
            ret_files.append(os.path.join(root, i))
    return ret_files


def main():
    import argparse
    import subprocess
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="the file to be renamed")
    args = parser.parse_args()
    subprocess.call(["mv", args.target, proper_name(args.target)])

if __name__ == "__main__":
    main()
