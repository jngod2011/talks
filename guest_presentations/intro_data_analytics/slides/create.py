#!/usr/bin/env python
"""This module compiles the notes with the figures."""
import subprocess
import shutil
import os

if __name__ == '__main__':

    for task in ['pdflatex']:
        subprocess.check_call(task + ' main', shell=True)
