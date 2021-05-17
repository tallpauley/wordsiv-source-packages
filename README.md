# Wordsiv Source Packages

This repository serves Python packages of [Sources](https://github.com/tallpauley/wordsiv/blob/main/wordsiv/source.py) for [Wordsiv](https://github.com/tallpauley/wordsiv), a text-generation library.

## Installing a Source Package
Source packages are Python packages, so you can simply install them with Pip.

Assuming you have already [installed Wordsiv](https://github.com/tallpauley/wordsiv#installation), you can install a Source package like this:

```bash
$ pip install https://github.com/tallpauley/wordsiv-source-packages/releases/download/en_wordcount_web-0.1.0/en_wordcount_web-0.1.0-py3-none-any.whl
```

## Modules to Packages

This source repository contains [Python modules](https://docs.python.org/3/tutorial/modules.html) with their accompanying `meta.json` files:

```text
en_wordcount_trigrams-0.1.0/
├── en_wordcount_trigrams
│   ├── __init__.py
│   └── data
│       └── data.lfs.txt
└── meta.json
```

These modules are packaged using the Wordsiv CLI, and then uploaded as individual Github Releases.

```bash
$ wordsiv package build modules/en_wordcount_trigrams-0.1.0 dist/
$ ls dist/
en_wordcount_trigrams-0.1.0-py3-none-any.whl
en_wordcount_trigrams-0.1.0.tar.gz
```

## Source Package Structure

Each package contains one module, which exports dicts `sources` and `meta`.

`sources` has the following structure, where `source` is a [Source](https://github.com/tallpauley/wordsiv/blob/main/wordsiv/source.py) object, and `default_model_class` is the default model to use with this source.

```python

sources = {
    "en_markov_gutenberg": {
        "source": MarkovSource(HERE / "data" / "data.lfs.json"),
        "default_model_class": MarkovModel,
    },
}

```

## Contributing

### Use Git LFS For Data Files

This repository uses [Git LFS](https://git-lfs.github.com/) to manage data files. This allows data files to get big without the Git repository itself getting huge.

We use the convention `filename.lfs.ext` for data files to make it simple to track these files with Git LFS.

#### Setup Git LFS

1. [Install Git LFS](https://git-lfs.github.com/)

    If you have [Homebrew](https://brew.sh/) it's:

    ```bash
    $ brew install git-lfs
    ```

2. Initialize Git LFS for your user acccount:

    ```bash
    $ git lfs install
    Updated git hooks.
    Git LFS initialized.
    ```

3. When you add a file such as `data.lfs.json`, double check it's being tracked by Git LFS. You willl see `LFS` to the right of the filename:

    ```bash
    $ git add data.lfs.json
    $ git lfs status

    Objects to be committed:

            data.lfs.json (LFS: 33d72bf)

    Objects not staged for commit:
    ```

4. Now you can commit, push, and pull request as normal!
