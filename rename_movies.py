import os
import subprocess

 _TARGET = '/Users/user/stuff/'
_VIDEO_TYPE = '\.(mkv|mp4|avi|mov)'
_YEAR = '\(?[1|2][0-9][0-9][0-9]\)?'

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

def proper_title(old_title):
    import re
    # find movie title
    # get rid of beginning number
    #print "working on ", old_title
    temp = old_title.split("-", 1)[1]

    # when the year comes before the title
    #mov_title = re.split(_YEAR, temp[1])
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


# get the list of absolute paths of all the movies
all_files = files_in_dir(_TARGET)

# take the basename and create a new basename
for f in all_files:
    print "-------------------"
    dirname = os.path.dirname(f)
    basename = os.path.basename(f) 
    new_base = proper_title(basename)
    new_path = os.path.join(dirname, new_base)
     
    subprocess.check_call(['mv', f, new_path])
    print "Moving"
    #print os.path.basename(f)
    print f
    print "to"
    # print os.path.basename(new_path)
    print new_path
    print
    print "--------------------"


