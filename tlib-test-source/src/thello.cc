/**
 * @mainpage
 * thello program.  Please see @ref thello.cc for more details.
 *
 * @file thello.cc
 * @brief Summary of thello
 * 
 * More detailed description.
 * @todo find a better solution to the mainpage problem.
 */

#include <stdio.h>
#include <iostream>

#include "thlib/thlib.h"
#include "thello-version.h"
#include "tmisc/tmisc.h"

int main(int argc, char **argv)
{
  printf("Hello, world -- %s version %s.%s.%s\n",thello_NAME, thello_MAJOR,thello_MINOR,thello_MICRO);
  printf(" tlib-test\n");
  printf(" tmisc version %s\n",tmisc::version());
  printf("argc %d\n",argc);
  for(int i=0; i<argc; i++)
    {
      printf(" arg[%d] %s\n",i,argv[i]);
    }

  printf("bundle path %s\n",thlib::getBundlePath());
  printf("asset path %s\n",thlib::getAssetPath());

  auto help_file = thlib::openFile(thlib::getAssetPath(), "help.txt", "r");

  if(!help_file)
    {
      printf("Was not able to open asset help.txt\n");
      fflush(stdout);
      exit(1);
    }

  char line[512];

  printf("help file:\n");
  while(fgets(line, 512, help_file))
    {
      printf("%s",line);
    }
  fclose(help_file);
  fflush(stdout);

  auto dict_file = thlib::openFile(thlib::getAssetPath(), "project.dict", "r");
  if(!dict_file)
    {
      exit(1);
    }
  printf("dict file:\n");
  while(fgets(line, 512, dict_file))
    {
      printf("%s",line);
    }
  fclose(dict_file);
  fflush(stdout);

  return 0;
}
