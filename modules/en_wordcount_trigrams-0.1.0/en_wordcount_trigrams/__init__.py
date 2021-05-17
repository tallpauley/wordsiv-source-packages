import pkgutil
import json
from wordsiv.sentence_models_sources import (
    WordCountSource,
    SequentialModel,
    RandomModel,
)
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
    "en_wordcount_trigrams": {
        "source": WordCountSource(HERE / "data" / "data.lfs.txt", meta),
        "default_model_class": SequentialModel,
    },
}