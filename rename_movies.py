import tcnfilemanagement
import os
import subprocess
import argparse

## THIS IS BROKEN

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("targetsdir", help="the directory with the files to be renamed")

    args = parser.parse_args()

    # get the list of absolute paths of all the movies
    all_files = files_in_dir(args.targetsdir)

    # take the basename and create a new basename
    for f in all_files:
        dirname = os.path.dirname(f)
        basename = os.path.basename(f)
        new_base = proper_title(basename)
        new_path = os.path.join(dirname, new_base)

        os.rename(f, new_path)

if __name__ == '__main__':
    main()
