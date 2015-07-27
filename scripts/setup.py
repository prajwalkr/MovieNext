from distutils.core import setup
import py2exe, sys, os

setup( 
  options = {         
    'py2exe' : {
        'compressed': 1, 
        'optimize': 2,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': '',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        }
        },                   
  zipfile=None, 
  console = ['main.py'],
)