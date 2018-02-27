import tcnfilemanagement
import os

## THIS IS BROKEN

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("targetsdir", help="the directory with the files to\
                        be renamed")
    parser.add_argument("--suffix", help="optional suffix")
    parser.add_argument("--dry", help="dry run, no files renamed",
                        action="store_true")

    # define a global variable that contains all parsed arguments
    args = parser.parse_args()

    # ensure that input target directory is actually a directory
    if not os.path.isdir(args.targetsdir):
        print args.targetsdir, "is not a directory, please enter a directory!"
        return -1

    # get the full path of all the files in the target directory
    files = files_in_dir(args.targetsdir)

    # filter out files aren't tv show episodes
    shows = return_just_shows(files)

    for path in shows:
        new_path = create_new_path(path)
        if args.dry:
            pass
        else:
            os.rename(path, new_path)
        print
        print path
        print "HAS BEEN MOVED TO"
        print new_path
        print

if __name__ == '__main__':
    main()
