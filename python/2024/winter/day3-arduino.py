#!/usr/bin/env python3

# Written by Yankai Zhu
# This python script is designed to be run on an account on the CSE machines


import subprocess
import shutil
import textwrap
import git


def main():
    # Fix "Firefox is already running but it is not responding. To open a new window, you must first close the existing firefox process or restart your system."
    subprocess.run("pkill -U $USER -f firefox", shell=True)
    subprocess.run("rm -rf .mozilla/firefox/*.default/.parentlock", shell=True)
    subprocess.run(
        'firefox "https://docs.google.com/presentation/d/1Yqk1hf7OoGZCTgLDs_NqrnPLsaZ_eI8eNcheF44jLns/edit" & disown',
        shell=True,
        executable="/bin/bash",  # we need to set to bash to make disown work
    )

    repos = ["2024-Winter-Arduino-Day3"]

    for repo in repos:
        try:
            git.Repo.clone_from(
                f"https://github.com/CSESoc-CompClub/{repo}", "Arduino", branch="deploy"
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

    subprocess.run(
        "./arduino-ide_2.3.2_Linux_64bit.AppImage --app-project-path Arduino/Blink & disown",
        shell=True,
        executable="/bin/bash",
    )


if __name__ == "__main__":
    main()
