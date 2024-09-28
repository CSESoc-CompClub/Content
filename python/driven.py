#!/usr/bin/env python3

# Written by Yankai Zhu
# Original bash script written by Thomas Liang
# This python script is designed to be run on an account on the CSE machines


import textwrap
import os
import shutil
import stat
import subprocess


def main():
    # Only run this if we want to wipe a user folder because they have exceeded the quota
    # subprocess.run("rm -rf * .*", shell=True)

    autostart_path = ".config/autostart/terminal.desktop"
    os.makedirs(os.path.dirname(autostart_path), exist_ok=True)
    with open(autostart_path, "w+") as f:
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

    # arduino_ide_appimage = "arduino-ide_2.3.2_Linux_64bit.AppImage"
    # arduino_ide_appimage_path = (
    #     f"/import/kamen/6/z5482795/public_html/compclub/{arduino_ide_appimage}"
    # )
    # shutil.copyfile(arduino_ide_appimage_path, arduino_ide_appimage)
    # os.chmod(arduino_ide_appimage, 0o700)

    link_name = "day2"
    real_name = (
        "/import/kamen/6/z5482795/public_html/compclub/2024/spring/day2-discord-bot.py"
    )
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
