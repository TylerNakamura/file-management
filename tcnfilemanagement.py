import subprocess
import os
import re

## THIS IS BROKEN

# RegEx Definitions...
SHOW = '[Ss]\d{2}[Ee]\d{2}'
VIDEO_TYPE = '\.(mkv|mp4|avi|mov)'
SUBTITLE_FILE_TYPE = '\.(srt|sub|subtitle)'
YEAR = '\(?[1|2][0-9][0-9][0-9]\)?'

# INPUT - full path of target avi
# This will fuck up if there is .avi in the path and NOT only in the basename
# this is not confirmed to be working yet. EXPERIMENTAL
def convertavitomp4(f):
	subprocess.check_call(["avconv", "-i", f, "-c:v", "libx264", "-preset", "veryslow", "-c:a", "copy", f.replace(".avi", ".mp4")])


'''
    returns True if the file path is a subtitle file
    this is only defined by looking at the file extension
    a subtitle is defined as a file matching the RegEx above
    returns true if the regex is found in the base name of the file path
'''
def is_subtitle_file(file_path):
    # get the file name of the full path
    file_name = os.path.basename(file_path)

    if re.search(SHOW, file_name) is not None:
        return True
    else:
        return False

'''
    returns True if the file path is a show
    a show is defined as a file matching the REGEX
    returns true if the regex is found in the base name of the file path
'''
def is_show_file(file_path):
    # get the file name of the full path
    file_name = os.path.basename(file_path)

    # if the regex matches both a show name and a video type in name...
    if re.search(SHOW, file_name) is not None and \
        re.search(VIDEO_TYPE, file_name) is not None:
        return True
    else:
        return False

'''
    input: a list of file names with full system paths
    returns a file list with only files that are tv show episodes
'''
def return_just_shows(files):
    shows = []
    for file in files:
        if is_show(file):
            shows.append(file)
    return shows

'''
    input: a movie title that is most likely incorrect
    this title contains a year
    for example: Cool Beans1980
    should return: Cool Beans (1980)
    TODO: can't handle "The summer of 1969 (1970)"
'''
def proper_title(old_title):
    # find movie title
    # get rid of beginning number
    temp = old_title.split("-", 1)[1]

    # when the year comes before the title
    # mov_title = re.split(_YEAR, temp[1])
    # when the comes after the title...
    mov_title = temp.split(".")[0]

    cap_mov_title = mov_title.title()
    cap_mov_title = cap_mov_title.replace(".", " ")
    cap_mov_title = re.sub(' +',' ',cap_mov_title)
    cap_mov_title = cap_mov_title.strip()

    # find year
    year_search = re.search(_YEAR, old_title)

    # find file type
    file_type = re.search(_VIDEO_TYPE, old_title, re.IGNORECASE)
    ret_string = ""
    ret_string += cap_mov_title
    ret_string += " "
    if "(" not in old_title:
        ret_string += "("
    ret_string += year_search.group()
    if ")" not in old_title:
        ret_string += ")"
    ret_string += file_type.group()

    # removing double spaces
    ret_string = re.sub("\s\s+", " ", ret_string)

    return ret_string


'''
    returns the full file path of all the files in input directory
    this function works recursively on a directory
'''
def files_in_dir(directory):
    ret_files = []
    for root, dirs, files in os.walk(directory):
        for i in files:
            ret_files.append(os.path.join(root, i))
    return ret_files


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
