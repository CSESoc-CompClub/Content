#!/usr/bin/env python3

# Written by Yankai Zhu
# This python script is designed to be run on an account on the CSE machines


import subprocess
import shutil
import textwrap
import traceback
from git import Repo


def main():
    # Fix "Firefox is already running but it is not responding. To open a new window, you must first close the existing firefox process or restart your system."
    subprocess.run("pkill -U $USER -f firefox", shell=True)
    subprocess.run("rm -rf .mozilla/firefox/*.default/.parentlock", shell=True)
    # TODO this link below might not be publically accessible :skull:
    subprocess.run(
        'firefox "https://docs.google.com/presentation/d/139Tm8D5wFW5SxegEdvirU2dfdPFAWULku23YoVpiZhc" & disown',
        shell=True,
        executable="/bin/bash",  # we need to set to bash to make disown work
    )

    # TODO check if need to open another firefox window with the guiding website

    repos = [""]

    for repo in repos:
        dir_name = f"compclub-{repo}"
        # shutil.rmtree(dir_name, ignore_errors=True)
        try:
            Repo.clone_from(f"https://github.com/CSESoc-CompClub/{repo}", dir_name)
        except Exception:
            print(
                textwrap.dedent(
                    f"""\
                    Failed to clone {repo} (probably because one already exists)
                    Ask a mentor for help and show them this the error message below
                    """
                )
            )

            traceback.print_exc()

        subprocess.run(f"code {dir_name}", shell=True, capture_output=True, text=True)


if __name__ == "__main__":
    main()
