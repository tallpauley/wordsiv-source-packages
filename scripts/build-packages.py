#!/usr/bin/env python3

from pathlib import Path
import shutil
import os
from os.path import basename

HERE = Path(__file__).parent.absolute().resolve()
BUILD_DIR = HERE.parent / 'build'
DATA_DIR = HERE.parent / 'data-source-packages'
PKG_COMMON_DIR = HERE.parent / 'package-common'

shutil.rmtree(BUILD_DIR, ignore_errors=True)
os.makedirs(BUILD_DIR, exist_ok=True)

for d in os.listdir(DATA_DIR):
    src_dir = DATA_DIR / d
    dest_dir = BUILD_DIR / d
    shutil.copytree(src_dir, dest_dir)

    # copy in common files
    for d2 in os.listdir(PKG_COMMON_DIR):
        shutil.copy(PKG_COMMON_DIR / d2, dest_dir)
