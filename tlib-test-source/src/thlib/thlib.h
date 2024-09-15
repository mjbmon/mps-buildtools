#ifndef THLIB_H
#define THLIB_H 1

namespace thlib
{
const char *getBundlePath();
const char *getAssetPath();
FILE *openFile(const char *base_path, const char *file_name, const char *flags);

}  // namespace thlib

#endif
