import pkgutil
from wordsiv.sentence_models_sources import MarkovSource, MarkovModel, WordCountSource, SequentialModel, RandomModel
from pathlib import Path
import json

# Assuming installed as directory (zip_safe=False)
HERE = Path(__file__).parent.absolute()

# meta.json will be copied into the module by setup.py
with open(HERE / "meta.json", "r") as f:
    meta = json.load(f)

# Sources should always be prefixed with the package name
# as they will be merged into a common namespace
sources = {
    "chr_markov": {
        "source": MarkovSource(HERE / "data" / "markov.lfs.json", meta),
        "default_model_class": MarkovModel,
    },
    "chr_words": {
        "source": WordCountSource(HERE / "data" / "word-list.lfs.txt", meta),
        "default_model_class": RandomModel,
    },
    "chr_trigrams": {
        "source": WordCountSource(HERE / "data" / "trigrams.lfs.txt", meta),
        "default_model_class": SequentialModel,
    },
}
