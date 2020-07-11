#!/usr/bin/env python3

import os, glob
from PIL import Image

newsize = 128, 128
# because we do not know what's in the file we use glob
for file in glob.glob("ic_*"):
       # open the file and convert to RGB
       im = Image.open(file).convert('RGB')
       im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")
