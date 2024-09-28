#!/usr/bin/env python3

# Written by Yankai Zhu
# This python script is designed to be run on an account on the CSE machines


import os
import subprocess
import shutil
import textwrap
import traceback
from git import Repo


def main():
    # Fix "Firefox is already running but it is not responding. To open a new window, you must first close the existing firefox process or restart your system."
    print("Attempting to kill any residue Firefox processes")
    subprocess.call("pkill -U $USER -f firefox", shell=True)
    subprocess.call("rm -rf .mozilla/firefox/*.default/.parentlock", shell=True)
    subprocess.call(
        'firefox "https://docs.google.com/presentation/d/1lF2fvBFgSQTUZaVq_ze7nw8zpmtS2ChZq7gclbysruc/edit?usp=sharing" & disown',
        shell=True,
        executable="/bin/bash",  # we need to set to bash to make disown work
    )

    root_repo = "Compclub-spring2024-discordjs"
    # shutil.rmtree(dir_name, ignore_errors=True)
    try:
        print(f"Cloning root repo {root_repo}")
        Repo.clone_from(
            f"https://github.com/tasdvl/{root_repo}", root_repo, branch="starter-code"
        )
    except Exception:
        print(
            textwrap.dedent(
                f"""\
                Failed to clone {root_repo} (probably because one already exists)
                Ask a mentor for help and show them this the error message below
                """
            )
        )

        traceback.print_exc()

    branches = ["grass-toucher", "vocabulary-trainer", "Joke-Candy-Bot", "jumpscare"]
    # Leave here for the future
    sanitised_branches = [branch.replace("/", "-") for branch in branches]

    for branch, sanitised_branch in zip(branches, sanitised_branches):
        clone_path = f"{root_repo}/{sanitised_branch}"
        os.makedirs(clone_path, exist_ok=True)

        try:
            print(f"Cloning branch {branch}")
            Repo.clone_from(
                f"https://github.com/tasdvl/{root_repo}", clone_path, branch=branch
            )
        except Exception:
            print(
                textwrap.dedent(
                    f"""\
                    Failed to clone branch {branch} (probably because one already exists)
                    Ask a mentor for help and show them this the error message below
                    """
                )
            )

            traceback.print_exc()

    print(f"Installing nvm")
    subprocess.call(
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash",
        shell=True,
        executable="/bin/bash",
    )
    subprocess.call(
        """export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && nvm install v20.17.0""",
        shell=True,
        executable="/bin/bash",
    )

    print(f"Installing npm packages")
    subprocess.call(
        "npm install",
        shell=True,
        executable="/bin/bash",
        cwd=root_repo,
    )

    print(f"Opening {root_repo} in VS Code")
    subprocess.call(
        f"code {root_repo}",
        shell=True,
        text=True,
        executable="/bin/bash",
    )

    print(f"Opening {root_repo}/setup-guide.md in VS Code")
    subprocess.call(
        f"code {root_repo}/setup-guide.md --reuse-window",
        shell=True,
        text=True,
        executable="/bin/bash",
    )


if __name__ == "__main__":
    main()
