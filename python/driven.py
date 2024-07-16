#!/usr/bin/env python3

# Written by Yankai Zhu
# Original bash script written by Thomas Liang
# This python script is designed to be run on an account on the CSE machines


import textwrap
import os
import shutil
import stat


def main():
    try:
        os.remove("compclub-intro")
    except:
        pass

    try:
        os.remove("cc-setup")
    except:
        pass

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

    arduino_ide_appimage = "arduino-ide_2.3.2_Linux_64bit.AppImage"
    arduino_ide_appimage_path = (
        f"/import/kamen/6/z5482795/public_html/compclub/{arduino_ide_appimage}"
    )
    shutil.copyfile(arduino_ide_appimage_path, arduino_ide_appimage)
    # We don't need to touch permissions at all

    link_name = "day3"
    real_name = (
        "/import/kamen/6/z5482795/public_html/compclub/2024/winter/day3-arduino.py"
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
