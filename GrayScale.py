#!/usr/bin/env python
import sys
from PIL import Image

param_1= sys.argv[1] 
img = Image.open(param_1).convert('LA')
img.save('grayscale.png')