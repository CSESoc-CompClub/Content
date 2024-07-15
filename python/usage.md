# Overview

The `driver.py` script creates a threadpool with a customisable number of threads and spawns a new shell for each (guest) account and runs `driven.py` from that guest account. At the moment, `driven.py` will create an autostart file (see [here](https://wiki.archlinux.org/title/Desktop_entries) for more details) for the terminal and also create a symlink in the (guest) user's home directory. The symlink points to the `setup.py` file and has the `cc-setup` name. It's possible to set up multiple setup files; just make sure the appropriate permissions (read + execute) are set.

When making modifications, you should always test the changes on an account like `cseguest00` first before deploying it to ALL (guest) users.

# Deploying

Put the correct password into the password file. Make sure there is a trailing newline. We put the password into a file to prevent leaking it through the process list as everyone can see invocation details.

Run `scp driver.py driven.py setup.py password z5482795@cse.unsw.edu.au:/import/kamen/6/z5482795/public_html/compclub` with your own zID to copy the files locally to the server using SSH.

You should then run

- `chmod 700 driver.py` (we do not want students running the code in this file)
- `chmod 755 driven.py` (needs to be readable + executable by other users)
- `chmod 755 setup.py` (needs to be readable + executable by other users)

Then just run `./driver.py` from your account.

You should see an output like

```
Starting 8 threads for 120 users...
cseguest04 returned 0
cseguest03 returned 0
cseguest00 returned 0
cseguest02 returned 0
cseguest07 returned 0
...
```

A return code of 0 means the `driven.py` script executed successfully. If there were any issues creating the (guest) user shells then this code won't be 0. If there were any uncaught exceptions in `driven.py`, then the code won't be 0 (I think). Also it's normal to see the (guest) user accounts out of order because we are using a threadpool.

For debugging you can comment out the `stdout=devnull, stderr=devnull` part of the subprocess creation call.

# pip packages on CSE

Running `pip freeze` on CSE machines gives us a list of pip packages installed on CSE. We can use these packages when writing scripts to be deployed on CSE machines.
