#!/usr/bin/env python3

# Written by Yankai Zhu
# Original bash script written by Thomas Liang
# This python script is designed to be run on an account on the CSE machines


import subprocess
import shutil
import textwrap
from git import Repo


def main():
    repos = ["2024-winter-clang-day2"]

    for repo in repos:
        dir_name = f"compclub-{repo}"
        # shutil.rmtree(dir_name, ignore_errors=True)
        try:
            Repo.clone_from(f"https://github.com/CSESoc-CompClub/{repo}", dir_name)
        except:
            print(
                textwrap.dedent(
                    f"""\
                    Failed to clone {repo} (probably because one already exists)
                    Ask a mentor for help and show them this message
                    """
                )
            )

        subprocess.run(f"code {dir_name}", shell=True, capture_output=True, text=True)


if __name__ == "__main__":
    main()
