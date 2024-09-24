import sys
import os
import random
import PIL
import numpy as np

from utils import processing

path = "change\\this\\to\\your\\dir"

processor = processing.Processor()
processor.run_processor(path)
