#!/usr/bin/env python3

# Written by Yankai Zhu
# Original bash script written by Thomas Liang
# This python script is designed to be run on an account on the CSE machines


import subprocess
import threading
from queue import Queue
import os


NUM_THREADS = 16
USER_LOWER_INCLUSIVE = 0
USER_UPPER_EXCLUSIVE = 120
DRIVEN_PATH = "/import/kamen/6/z5482795/public_html/compclub/driven.py"

devnull = open(os.devnull, "w")


def worker(queue):
    while not queue.empty():
        user = queue.get()
        if user is None:
            break
        execute_script(user)
        queue.task_done()


def execute_script(user):
    username = f"cseguest{str(user).zfill(2)}"
    command = f"cat password | su --login {username} -c {DRIVEN_PATH}"
    try:
        result = subprocess.run(command, shell=True)
        print(f"{username} returned {result.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"Failed for {username}: {e.stderr}")


def main():
    queue = Queue()

    for user in range(USER_LOWER_INCLUSIVE, USER_UPPER_EXCLUSIVE):
        queue.put(user)

    print(
        f"Starting {NUM_THREADS} threads for {USER_UPPER_EXCLUSIVE - USER_LOWER_INCLUSIVE} users..."
    )

    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker, args=(queue,))
        thread.start()
        threads.append(thread)

    queue.join()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
