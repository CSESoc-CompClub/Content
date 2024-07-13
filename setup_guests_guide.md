## Usage

<aside>
💢 **MAKE SURE TO `chmod -R 755` EVERYTHING IN PUBLIC HTML!!!!**

</aside>

1. Put it in `public_html` on your uni account
2. make a folder for your wo  rkshop (e.g. intro)
3. make a script `public_html/intro/setup`

```bash
#!/bin/bash
# mksetup - A (real) example setup script you might pass to setupguests.

cd $HOME

cat <<eof > intro
#!/bin/bash
bash <(curl -sSL go.compclub.org/scripts/intro-py)
eof
chmod +x intro

mkdir -p .config/autostart
cat <<eof > .config/autostart/terminal.desktop
[Desktop Entry]
Type=Application
Name=automatically open a terminal
Hidden=false
Exec=x-terminal-emulator
eof
```

1. make a script `public_html/intro/intro.sh`

```bash
#!/bin/bash

# CompClub Spring Workshops 2023
# Intro to Linux and C++

REPO="2024-Autumn-Python-Intro"
PREFIX="$(pwd)/intro_to_pygame"

if [ -f $PREFIX ]
then
	echo "$PREFIX is a file not a directory!!"
fi

if [ ! -d $PREFIX ]
then
	wget "https://github.com/CSESoc-CompClub/$REPO/archive/refs/heads/dist.zip"
	unzip main.zip
	rm main.zip
	mv "$REPO-main" $PREFIX
	cd $PREFIX
fi

code $PREFIX
```

1. use [short.io](http://short.io) to link `intro-py` (or whatever your slug is) to your `public_html/intro/intro.sh`
2. run `./setupguests intro/setup $(seq 100 175)` (obviously replace your range), password is `CSE2019b`
