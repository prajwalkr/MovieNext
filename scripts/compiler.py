from py_compile import compile
from os.path import *
compile(join(dirname(dirname(__file__)),'main.py'))