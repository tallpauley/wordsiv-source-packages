import pkgutil
from wordsiv.models.markov_model import Model, MarkovSource
from pathlib import Path

# Assuming installed as directory (zip_safe=False)
HERE = pathlib.Path(__file__).parent.absolute()

sources = [
    "default": MarkovSource(HERE / 'data/data.lfs.json')
]