import sys
import os
import random
import PIL
import numpy as np

from utils import processing

path = "I:\\人工智能研究院\\线束项目\\202408ComponentsDataset\\images"

processor = processing.Processor()
processor.run_processor(path)
