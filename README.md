# Wordsiv Data Packages

This repository contains the data and metadata to build packages for [Wordsiv](https://github.com/tallpauley/wordsiv) text generation library.

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
