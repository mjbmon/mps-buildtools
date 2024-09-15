#
# Try to read a file and parse some lines like PROGRAM_VERSION_MAJOR
#

import os, sys
import argparse
import re

def check_name(name):
  if(re.match('^[a-z][a-z0-9-]*$', name)):
    return False
  return True

def check_number(number):
  if(re.match('^[0-9]*$', number)):
    return False
  return True

if __name__=="__main__":

# I should add --name, --major, --minor, --micro, --pkg to get the
# project name, major, minor, micro, and full package names.
#
# Parse command line arguments
  parser = argparse.ArgumentParser(description='Get project name and version.')
  parser.add_argument('--all', action='store_true', help='Print all components')
  parser.add_argument('cmake', help='CMakeLists.txt file')
  args = parser.parse_args()

  cname = args.cmake
#  print("File ", cname)

  the_project_name = None
  the_project_major = None
  the_project_minor = None
  the_project_micro = None

  with open(cname) as cfile:
    for line in cfile:
      m = re.search('(THE_PROJECT_[A-Z]*) ("[^"]*")', line)
      if m:
       if(m.group(1) == 'THE_PROJECT_NAME'):
         the_project_name = m.group(2).strip('"')
       if(m.group(1) == 'THE_PROJECT_MAJOR'):
         the_project_major = m.group(2).strip('"')
       if(m.group(1) == 'THE_PROJECT_MINOR'):
         the_project_minor = m.group(2).strip('"')
       if(m.group(1) == 'THE_PROJECT_MICRO'):
         the_project_micro = m.group(2).strip('"')

# This is the convention for Debian upstream package names:
#   Package names (both source and binary, see Package) must consist only
#   of lower case letters (a-z), digits (0-9), plus (+) and minus (-) signs,
#   and periods (.). They must be at least two characters long and must
#   start with an alphanumeric character.
#
# The major and minor fields must be digits only. Cmake requires that the
# micro field be only digits also.
#
# This tool should check the project name, ... to make sure that the
# convention is followed.
# 
# I am going to only allow names that do not have periods.
#
  if(check_name(the_project_name)):
    print("PROJECT NAME VIOLATES NAME CONVENTION ", the_project_name)
  if(check_number(the_project_major)):
    print("PROJECT MAJOR IS NOT A NUMBER", the_project_major)
  if(check_number(the_project_minor)):
    print("PROJECT MINOR IS NOT A NUMBER", the_project_minor)
  if(check_number(the_project_micro)):
    print("PROJECT MICRO IS NOT A NUMBER", the_project_micro)


  the_project_string = the_project_name + "_" + the_project_major + "." + the_project_minor + "." + the_project_micro

  if(args.all):
    print("PROJECT NAME   ", the_project_name)
    print("PROJECT MAJOR  ", the_project_major)
    print("PROJECT MINOR  ", the_project_minor)
    print("PROJECT MICRO  ", the_project_micro)
    print("PROJECT STRING ", the_project_string)
  else:
    print(the_project_string)

