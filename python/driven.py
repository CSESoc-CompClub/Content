#!/usr/bin/env python3

# Written by Yankai Zhu
# Original bash script written by Thomas Liang
# This python script is designed to be run on an account on the CSE machines


import textwrap
import os


def main():
    with open(".config/autostart/terminal.desktop", "w") as f:
        f.write(
            textwrap.dedent(
                """\
                [Desktop Entry]
                Type=Application
                Name=automatically open a terminal
                Hidden=false
                Exec=x-terminal-emulator
                """
            )
        )

    link_name = "cc-setup"
    real_name = "/import/kamen/6/z5482795/public_html/compclub/setup.py"
    try:
        os.symlink(real_name, link_name)
    except:
        os.remove(link_name)
        try:
            os.symlink(real_name, link_name)
        except:
            print("Failed to create symlink")

        pass


if __name__ == "__main__":
    main()
