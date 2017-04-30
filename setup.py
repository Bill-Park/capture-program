from distutils.core import setup
import py2exe

setup(
    console=['screen.py'],
    option = {
        'py2exe': {
            'includes': ['test_ui, bill'],
            'packages': ['PyQt5, sys, os'],
        }
    },
    zipfile=None,
)
