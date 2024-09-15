import os
import subprocess
import argparse
from pathlib import Path
import json
import re

if __name__=="__main__":

# Create the initial project dictionary
  project_dict = dict()

# Get home, cwd, source directory, and python def
  project_dict["HOME"] = str(Path.home())
  project_dict["PROJECT_WORK_DIR"] =  os.getcwd()
  project_dict["PROJECT_BUILD_DIR"] =  "./build.dir"
  if os.name == "nt":
    project_dict["PROJECT_BUILD_DIR"] =  ".\\build.dir"

  top = os.getenv('PROJECT_TOP_DIR')
  if top == None:
    print("Cannot get PROJECT_TOP_DIR")
    os.exit(1)
  project_dict["PROJECT_TOP_DIR"] = os.path.abspath(top)

  py = os.getenv('PYTHON')
  if py == None:
    print("Cannot get PYTHON")
    os.exit(1)
  project_dict["PYTHON"] = py

  bt =  os.getenv('MPS_BUILDTOOLS')
  if bt == None:
    print("Cannot get MPS_BUILDTOOLS")
    os.exit(1)
  project_dict["MPS_BUILDTOOLS"] = bt

# TO DO: 
#
#   Check that (src)/templates and (src)/src exist
#   Check and warn if PROJECT_TOP_DIR and WORK_DIR are the same
#

# TO DO: other variables defined in the configure or configure.bat templates

# Parse command line arguments
#
# --prefix  set PROJECT_INSTALL_PREFIX
# --build   set PROJECT_BUILD_CONFIG

# Set universal defaults. Do not change these
# for a project. Instead, write a (source)/templates/project_initial.dict
# file, see below.
# TO DO: document reasoning for these settings
# On windows default should be .\install etc.

  DEFAULT_INSTALL_PREFIX=project_dict["HOME"]+"/.local"
  if os.name == "nt":
    DEFAULT_INSTALL_PREFIX=project_dict["HOME"]+"\\.local"
  DEFAULT_BUILD_CONFIG="Release"

  project_dict["PROJECT_INSTALL_PREFIX"] = DEFAULT_INSTALL_PREFIX
  project_dict["PROJECT_BUILD_CONFIG"] = DEFAULT_BUILD_CONFIG

# Read the (src)/project_initial.dict file if it exists
  dfile = project_dict["PROJECT_TOP_DIR"] + "/templates/project.dict"
  if os.path.isfile(dfile):
    with open(dfile, "r") as fp:
      vars = json.load(fp)
    project_dict.update(vars)

# Parse command line arguments
  parser = argparse.ArgumentParser(description='Configure project.')
  parser.add_argument('--prefix', default=project_dict["PROJECT_INSTALL_PREFIX"], help='Set the install prefix')
  parser.add_argument('--build', default=project_dict["PROJECT_BUILD_CONFIG"], help='Set the build configuration')
  args = parser.parse_args()

# TO DO:
#   add a --toolchain argument
#

# Set install prefix and build config
  project_dict["PROJECT_INSTALL_PREFIX"] = args.prefix
  project_dict["PROJECT_BUILD_CONFIG"] = args.build

# Read the (build)/project_initial.dict file if it exists. This
# lets the developer override everything for non-standard build.
# The developer can just do a configure, then copy project.dict to
# project_initial.dict, and after that configure with no arguments.
  dfile = project_dict["PROJECT_WORK_DIR"] + "/project_initial.dict"
  if os.path.isfile(dfile):
    with open(dfile, "r") as fp:
      vars = json.load(fp)
    project_dict.update(vars)

  cname = project_dict["PROJECT_TOP_DIR"] + "/src/CMakeLists.txt"

# Parse the CMakeLists file for lines that look like
#   set(THE_PROJECT_X "VALUE") (quotes required).
# Note: This cannot resolve computed variables. So
# set(THE_PROJECT_X "${SOME_VAR}" ) or anything like it will not work.
  if os.path.isfile(cname):
    with open(cname) as cfile:
      for line in cfile:
        m = re.search('(THE_PROJECT_[A-Z]*) ("[^"]*")', line)
        if m:
          mname = m.group(1).strip('"')
          mval  = m.group(2).strip('"')
          project_dict[mname] = mval

  else:
    print("WARNING: CMakeLists.txt file not found.")
    printf( cfile);



# Write the project.dict file
  with open(project_dict["PROJECT_WORK_DIR"] + '/project.dict','w') as fp:
    json.dump(project_dict,fp)

# Process files to create Makefile or make.bat
#  tool_dir = project_dict["PROJECT_TOP_DIR"] + "/tools"
  tool_dir = project_dict["MPS_BUILDTOOLS"]
  ctool=tool_dir+'/config_tool.py'
  if os.name == "nt":
    subprocess.run([project_dict["PYTHON"], ctool, 'make.bat.in', 'make.bat'])
  else:
    subprocess.run([project_dict["PYTHON"], ctool, 'Makefile.in', 'Makefile'])

  print("Configuration is complete")
  print("For help on configuring, building and installing use 'make help'")
  print("To build, use 'make all'")
  print("To install, use 'make install'")
