#!/usr/bin/env python3

# Written by Yankai Zhu
# This python script is designed to be run on an account on the CSE machines


import subprocess
import shutil
import textwrap
import git


def main():
    repos = ["2024-Winter-Arduino-Day3"]

    for repo in repos:
        dir_name = f"compclub-{repo}"
        try:
            git.Repo.clone_from(
                f"https://github.com/CSESoc-CompClub/{repo}", dir_name, branch="deploy"
            )
        except:
            print(
                textwrap.dedent(
                    f"""\
                    Failed to clone {repo} (probably because one already exists)
                    Ask a mentor for help and show them this message
                    """
                )
            )

        # This is broken for now
        # subprocess.run(
        #     f"./arduino-ide_2.3.2_Linux_64bit.AppImage --app-project-path {dir_name}",
        #     shell=True,
        #     capture_output=True,
        #     text=True,
        # )


if __name__ == "__main__":
    main()
