import pkgutil
import json
from wordsiv.text_models.wordcount import (
    WordCountSource,
    TopModel,
    RandomModel,
    ProbabilityModel,
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
sources = {"en_wordcount_trigrams": WordCountSource(HERE / "data" / "data.lfs.txt")}

# dictionary of "pipelines": preset maps of sources to models
# Pipelines should also be prefixed with the package name
pipelines = {
    # basically an alias for en_wordcount_trigrams_top
    "en_wordcount_trigrams": {
        "source": sources["en_wordcount_trigrams"],
        "model_class": TopModel,
    },
    "en_wordcount_trigrams_top": {
        "source": sources["en_wordcount_trigrams"],
        "model_class": TopModel,
    },
    "en_wordcount_trigrams_random": {
        "source": sources["en_wordcount_trigrams"],
        "model_class": RandomModel,
    },
    "en_wordcount_trigrams_prob": {
        "source": sources["en_wordcount_trigrams"],
        "model_class": ProbabilityModel,
    },
}
