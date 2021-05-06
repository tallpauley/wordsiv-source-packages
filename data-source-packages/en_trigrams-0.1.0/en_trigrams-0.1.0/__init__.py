import pkgutil
from wordsiv.sources import CountSource
from pathlib import Path

# Assuming installed as directory (zip_safe=False)
HERE = Path(__file__).parent.absolute()

sources = {
    'default': CountSource(HERE / 'data' / 'data.lfs.txt')
}