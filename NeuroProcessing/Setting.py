#modules
import pandas as pd
import numpy as np
import json
import os, sys
import scipy.io
from scipy import signal
import matplotlib.pyplot as plt
import statistics
import math
import gc
import warnings
from pathlib import Path
import re
import json
from typing import Literal, Tuple, List, Dict
import struct
from decimal import *
import csv
from tokenize import String



#numpyをjsonで出力できるように修正
class NumpyEncoder(json.JSONEncoder):
    """how to use
    numpy_structure=(** array or dict etc ... with numpy structure**)
    json.dumps(numpy_structrue , cls=NumpyEncoder)
    """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyEncoder, self).default(obj)


class PlotSetting():
    def __init__(self):
        with open("setting.json") as setting_file:
            self.xlim: list[float] = setting_file["xlim"]
            self.ylim: list[float] = setting_file["ylim"]
            self.channelmap: list[int] =setting_file["channelmap"]
            self.samplerate: int = setting_file["samplerate"]
            self.linewidth = setting_file["linewidth"]
            self.xlabel = setting_file["xlabel"]
            self.ylabel = setting_file["ylabel"]
            