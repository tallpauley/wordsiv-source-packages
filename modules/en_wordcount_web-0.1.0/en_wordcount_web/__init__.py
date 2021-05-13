import pkgutil
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
sources = {
    "en_wordcount_web": WordCountSource(
        HERE / "data" / "data.lfs.txt", 50000
    ),  # 50k default
    "en_wordcount_web_medium": WordCountSource(
        HERE / "data" / "data.lfs.txt", 50000
    ),  # 50k
    "en_wordcount_web_small": WordCountSource(
        HERE / "data" / "data.lfs.txt", 10000
    ),  # 10k
    "en_wordcount_web_large": WordCountSource(
        HERE / "data" / "data.lfs.txt"
    ),  # 1/3rd million(ish)
}

# dictionary of "pipelines": preset maps of sources to models
# Pipelines should also be prefixed with the package name
pipelines = {
    # basically an alias for en_wordcount_web_prob
    "en_wordcount_web": {
        "source": sources["en_wordcount_web"],
        "model_class": ProbabilityModel,
    },
    "en_wordcount_web_prob": {
        "source": sources["en_wordcount_web"],
        "model_class": ProbabilityModel,
    },
    "en_wordcount_web_top": {
        "source": sources["en_wordcount_web"],
        "model_class": TopModel,
    },
    "en_wordcount_web_random": {
        "source": sources["en_wordcount_web"],
        "model_class": RandomModel,
    },
}
