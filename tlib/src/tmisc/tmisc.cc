#include <stdio.h>
#include <tmisc/tmisc.h>

#include "tpriv.h"

static char *tmisc_version_string = nullptr;
static void setup_tmisc();

namespace tmisc
{

const char *version()
{
  setup_tmisc();
  return tmisc_version_string;
}

// implementation of tmps class
tmps::tmps(){}


} // namespace tmisc

static void setup_tmisc()
{
  if (tmisc_version_string) return;

  tmisc_version_string = new char[128];
//  snprintf(tmisc_version_string, 128, "%d.%d", TMISC_MAJOR, TMISC_MINOR);
  snprintf(tmisc_version_string, 128, "%s %s.%s", PROJECT_NAME, PROJECT_VERSION_MAJOR, PROJECT_VERSION_MINOR);
}
