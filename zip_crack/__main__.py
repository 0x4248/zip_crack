#!/usr/bin/env python3
# Zip crack
# A tool to crack zip files
# Github: https://www.github.com/awesomelewis2007/zip_crack
# Licence: GNU General Public Licence v3.0
# Author: Lewis Evans

import zipfile
import argparse
import sys
import os
import time
import tqdm
import shutil
from colorama import Fore, Back, Style


def crack(file, wordlist):
    start = time.time()
    password_is_found = False
    try:
        os.mkdir("temp")
    except FileExistsError:
        pass
    shutil.copyfile(file, "temp/" + file)
    time_taken = 0
    password_found = ""
    with open(wordlist, "r") as f:
        passwords = f.read().splitlines()
    os.chdir("temp")
    for password in tqdm.tqdm(passwords, desc="Cracking zip file", unit="password"):
        try:
            with zipfile.ZipFile(file) as zf:
                zf.extractall(pwd=password.encode())
                time_taken = str(time.time() - start)
                password_found = password
                password_is_found = True
                break
        except RuntimeError:
            pass
    if not password_is_found:
        print("Password not found")
        print("Time taken: " + str(time.time() - start))
    else:
        print("Password found: " + Fore.GREEN + password_found + Style.RESET_ALL)
        print("Time taken: ", time_taken)

    os.chdir("..")
    shutil.rmtree("temp")


if __name__ == "__main__":
    print("Welcome to zip_crack!")
    print("A tool to crack zip files")
    print("Only use this tool on zip files you have permission to crack")
    try:
        input("Press enter to continue or ctrl + c to exit")
    except KeyboardInterrupt:
        sys.exit(1)
    parser = argparse.ArgumentParser(description="A tool to crack zip files")
    parser.add_argument("-f", "--file", help="The zip file to crack", required=True)
    parser.add_argument("-w", "--wordlist", help="The wordlist to use", required=True)

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("The zip file does not exist")
        sys.exit(1)

    if not os.path.isfile(args.wordlist):
        print("The wordlist does not exist")
        sys.exit(1)

    crack(args.file, args.wordlist)
