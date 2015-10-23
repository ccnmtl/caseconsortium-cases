'''
  Find home page duplicates and delete them, then update links to the duplicate
'''
from subprocess import call
import os
import sys
import fileinput
import re


file_to_search = sys.argv[1]


def search_folders(file_name):
    orig_homepage = "case_id_\d+.html"
    dup_homepage = "case_id_\d+_id_\d+.html"
    for path, subdirs, files in os.walk(file_name):
        if path.endswith("layout"):
            files.sort()
            potential_dups = []
            for f_name in files:
                homematchObj = re.match(orig_homepage, f_name)
                dupmatchObj = re.match(dup_homepage, f_name)
                if homematchObj:
                    # print "match found for homepage file: "
                    print f_name
                else:
                    pass
                    # print "Not a homepage file"
                    # print f_name
                if dupmatchObj:
                    # print "match found duplicate homepage file: "
                    print f_name[:-5].split('_')[4]
                    potential_dups.append(f_name[:-5].split('_')[4])
                    temp = potential_dups[0]
                    for each in potential_dups:
                        if each < temp:
                            temp = each
                    print "lowest value file is"
                    print temp
                        
                else:
                    pass
                    # print "Not homepage duplicate"
                    # print f_name
                    
#                 '''Find home page, only has one id_*num*'''
#                 if "_pid_0" in f_name:
#                     print "Removing file : " + str(f_name)
#                     file_path = os.path.join(path, f_name)
#                     call(["git", "rm", file_path])

#     # go over directory second time - # of files
#     # to update should be smaller
#     for path, subdirs, files in os.walk(file_name):
#         files.sort()
#         for f_name in files:
#             if "case_id_" in f_name:
#                 print "Updating file " + str(f_name)
#                 file_path = os.path.join(path, f_name)
#                 old_string = "_pid_0.html"
#                 new_string = ".html"
#                 newfile = open(file_path, 'r+')
#                 for line in fileinput.input(file_path):
#                     newfile.write(line.replace(old_string, new_string))
#                 newfile.close()

search_folders(file_to_search)
