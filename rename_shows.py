import subprocess
import os
import re

# RegEx Definitions...
SHOW = '[Ss]\d{2}[Ee]\d{2}'
VIDEO_TYPE = '\.(mkv|mp4|avi|mov)'
SUBTITLE_FILE_TYPE = '\.(srt|sub|subtitle)'

'''
    returns True if the file path is a subtitle file
    a subtitle is defined as a file matching the RegEx above
    returns true if the regex is found in the base name of the file path
'''
def is_subtitle(file_path):
    # get the file name of the full path
    file_name = os.path.basename(file_path)

    if re.search(SHOW, file_name) is not None:
        print "Found that", file_name, "is a subtitle file..."
        return True
    else:
        print "Found that", file_name, "is a not a subtitle file..." 
        return False

'''
    returns True if the file path is a show
    a show is defined as a file matching the REGEX 
    returns true if the regex is found in the base name of the file path
'''
def is_show(file_path):
    # get the file name of the full path
    file_name = os.path.basename(file_path)

    # if the regex matches both a show name and a video type in name...
    if re.search(SHOW, file_name) is not None and \
        re.search(VIDEO_TYPE, file_name) is not None:
        print "Found that", file_name, "is a show..."
        return True
    else:
        print "Found that", file_name, "is a not show..." 
        return False
 
'''
    returns a file list with only files that are tv show episodes
'''
def return_shows(files):
    shows = []
    for file in files:
        if is_show(file):
            shows.append(file)
    return shows


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

'''
    rename each show to just the regex match
    takes in a list of absolute paths
'''
def rename_shows(shows):
    for path in shows:
        new_path = create_new_path(path)
        if args.dry:
            pass
        else:
            subprocess.check_output(['mv', path, new_path])
        print 
        print path 
        print "HAS BEEN MOVED TO"
        print new_path
        print

'''
    takes in the full path of a file, extracts the regex and returns a new path
'''
def create_new_path(show):
    # extract directory name
    dirname = os.path.dirname(show)
    
    # extract the file name
    basename = os.path.basename(show)

    # extract regex match of show name
    new_name = re.search(SHOW, basename)

    # extrct regex match of video type
    video_type = re.search(VIDEO_TYPE, basename)

    # if a suffix is specified, add suffx to the new path
    if args.suffix is not None:
        new_path = os.path.join(dirname, new_name.group(0) + '-' + args.suffix + video_type.group(0))
    else:
        new_path = os.path.join(dirname, new_name.group(0)+video_type.group(0))

    return new_path
     

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("targetsdir", help="the directory with the files to\
                        be renamed")
    parser.add_argument("--suffix", help="optional suffix")
    parser.add_argument("--dry", help="dry run, no files renamed",
                        action="store_true")

    # define a global variable that contains all parsed arguments
    global args
    args = parser.parse_args()

    # ensure that input target directory is actually a directory
    if not os.path.isdir(args.targetsdir):
        print args.targetsdir, "is not a directory, please enter a directory!"
        return -1     
    
    # get the full path of all the files in the target directory
    files = files_in_dir(args.targetsdir)
    
    # filter out files aren't tv show episodes
    shows = return_shows(files)

    # rename each file to just the regex match name
    rename_shows(shows)
    

if __name__ == '__main__':
    main()
