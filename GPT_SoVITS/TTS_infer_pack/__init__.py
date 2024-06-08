import sys
import os

# 将项目根目录添加到sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from . import TTS, text_segmentation_method