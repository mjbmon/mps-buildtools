#include <stdio.h>
#include <string.h>
#include <cstdlib>

#include "thlib.h"

#define MAX_PATH_LENGTH 1024

static char *bundle_path;
static char *asset_path;
static char file_name_buffer[MAX_PATH_LENGTH];
static void setup_bundle_paths();

namespace thlib
{

const char *getBundlePath()
{
  setup_bundle_paths();
  return bundle_path;
}

const char *getAssetPath()
{
  setup_bundle_paths();
  return asset_path;
}

FILE *openFile(const char *base_path, const char *file_name, const char *flags)
{
#ifdef _WIN32
  snprintf(file_name_buffer, MAX_PATH_LENGTH, "%s\\%s", base_path, file_name);
#else
  snprintf(file_name_buffer, MAX_PATH_LENGTH, "%s/%s", base_path, file_name);
#endif
  auto f = fopen(file_name_buffer, flags);
  if(!f)
    {
      printf("Was not able to open %s %s\n",file_name_buffer, flags);
    }
  return f;
}

} // namespace thlib

static void setup_bundle_paths()
{
  if(bundle_path) return;

  bundle_path = new char[MAX_PATH_LENGTH];
  asset_path = new char[MAX_PATH_LENGTH];

  auto bundle_dir = std::getenv("BUNDLE_DIR");
  if(bundle_dir == nullptr)
    {
      printf("BUNDLE_DIR env variable not set\n");
      exit(1);
    }
  strncpy(bundle_path, bundle_dir, MAX_PATH_LENGTH);  // NOLINT

  snprintf(asset_path, MAX_PATH_LENGTH, "%s/assets", bundle_path);

}
