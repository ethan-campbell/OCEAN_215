"""

This is a script to run iPython Notebook programming assignments through the MOSS plagiarism detection algorithm.
Ethan C. Campbell, for OCEAN 215 (Autumn 2017), University of Washington

#############

One-time setup instructions for macOS:

(1) obtain MOSS user ID by sending email to moss@moss.stanford.edu including only the following two lines of text:
            registeruser
            mail <<email@domain.suffix>>
    where <<...>> is your email address

(2a) in the automatic response email, look for your user ID (the line starts with '$userid=')
(2b) set the variable 'moss_user_id' to this number

(3) install Python client for MOSS using the following Terminal command (hopefully you have pip installed already):
            pip install mosspy

#############

Instructions for checking a batch of homework assignments:

(1) create an empty directory on your machine and save its path as the variable 'root_dir' below
    this is where both the iPython Notebooks will be stored, and the MOSS results will be saved

(2a) copy the original, blank assignment (an iPython Notebook) to this directory
(2b) save its filename as the variable 'original_assignment' below

(3a) copy all students' assignments (iPython Notebooks) to this directory
(3b) check that all assignments have a common string within their filenames, such as 'A1.215'
     if they don't, modify filenames to remedy this
(3c) save that common string as the variable 'submission_string' below

(4) run this script!

(5) similarity report (an HTML file) is linked in output; the report is also saved locally to the specified directory

"""

import mosspy
import os

# run parameters
moss_user_id = 181443923
root_dir = '/Users/Ethan/Desktop/MOSS/'
original_assignment = 'Assignment #2.py' # should end in .py
submission_string = 'graded'

# convert all Notebooks to Python scripts
os.system('jupyter nbconvert --to script {0}*.ipynb --to python'.format(root_dir))

# create new MOSS instance
m = mosspy.Moss(moss_user_id, 'python')

# set base assignment
m.addBaseFile(root_dir + original_assignment)

# submit files
# m.addFile(root_dir + 'single_assignment.py')
m.addFilesByWildcard(root_dir + '*{0}*.py'.format(submission_string))
url = m.send()

# save report file
print('MOSS report URL: ' + url)
m.saveWebPage(url, root_dir + 'report.html')

# download whole report locally including code diff links
mosspy.download_report(url, root_dir + 'report/', connections=8)
