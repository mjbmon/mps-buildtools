# This tool takes a dictionary and a template and produces an output
# file using jinja2.
# 
# Usage:
#    python config_tool.py OPTIONS TEMPLATE OUTPUT
#
#  OPTIONS:
#    --dict=DICTIONARY          json dictionary file
#    --template_path=TEMPLATE_PATH   path for templates
#    -Dname=value
#
#  DICTIONARY defaults to ./project.dict
#  TEMPLATE_PATH defaults to PROJECT_TOP_DIR/templates
#
#  If TEMPLATE_PATH is given as relative, it is relative
#  to PROJECT_TOP_DIR. Otherwise it is an absolute path.
# 

import os, sys
import re
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader
import argparse
import json

def process_file(template_dir, template_file, variable_list, output_file):
  ldr = FileSystemLoader(searchpath=template_dir)
  env = Environment(loader=ldr)
  tmp = env.get_template(template_file)
  text = tmp.render(variable_list)
  file = open(output_file, "w")
  file.write(text)
  file.close()

if __name__=="__main__":

# Parse command line arguments
  parser = argparse.ArgumentParser(description='Create file from template.')
  parser.add_argument('--dict', default=None, help='Set the dictionary file')
  parser.add_argument('--template_dir', default=None, help='Set the template directory')
  parser.add_argument('-D', default=None, action='append', help='Define variable')
  parser.add_argument('template', help='Template script file')
  parser.add_argument('output', help='Output file path')
  args = parser.parse_args()

  dict = "project.dict"
  if (args.dict != None) :
    dict = args.dict

  with open(dict, "r") as fp:
    vars = json.load(fp)

  d = args.D
  if d != None:
    for a in args.D:
      am = re.search('([a-zA-Z0-9_]*)=(.*)', a)
      vars[am.group(1)] = am.group(2)

  t=vars['PROJECT_TOP_DIR']
  if t == None:
    t='.'
  template_dir=t + '/templates'

  if (args.template_dir != None) :
    template_dir = args.template_dir

  template_file = args.template

  output_file = args.output

  process_file(template_dir, template_file, vars, output_file)

