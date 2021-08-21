import glob
import re
import os
# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = "./"
for filename in glob.iglob(root_dir + '**/*.png', recursive=True):

	path = filename.split("/")
	path[-1] = "Question.png"
	new_name = "/".join(path)
	print(new_name)
	os.rename(filename, new_name)
