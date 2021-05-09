import pkgutil
from wordsiv.models.markov import MarkovSource, MarkovModel
from pathlib import Path
import json

# Assuming installed as directory (zip_safe=False)
HERE = Path(__file__).parent.absolute()

# meta.json will be copied into the module by setup.py
with open(HERE / "meta.json", "r") as f:
    meta = json.load(f)

# Sources should always be prefixed with the package name
# as they will be merged into a common namespace
sources = {"en_markov_gutenberg": MarkovSource(HERE / "data" / "data.lfs.json")}

# dictionary of "pipelines": preset maps of sources to models
# Pipelines should also be prefixed with the package name
pipelines = {
    "en_markov_gutenberg": {
        "source": sources["en_markov_gutenberg"],
        "model_class": MarkovModel,
    }
}
