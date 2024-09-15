# showimage.py
#
# Usage:
#
#    python showimage.py IMAGE_FILE
#

import sys
from PIL import Image

if __name__=="__main__":
  image_filename = sys.argv[1]
  print(image_filename)
  image = Image.open(image_filename)
  image.show()
