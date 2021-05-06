import pkgutil
from wordsiv.sources import CountSource
from pathlib import Path

# Assuming installed as directory (zip_safe=False)
HERE = Path(__file__).parent.absolute()

# File is almost 1/3rd million words, so we limit this
sources = {
    'default': CountSource(HERE / 'data' / 'data.lfs.json', 100000), # 10k default
    'small': CountSource(HERE / 'data' / 'data.lfs.json', 10000), # 10k
    'medium': CountSource(HERE / 'data' / 'data.lfs.json', 100000), # 100k
    'large': CountSource(HERE / 'data' / 'data.lfs.json') # 1/3rd million(ish)
}