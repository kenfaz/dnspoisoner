"""
A script that replaces the /etc/hosts file 
of the current operating system and redirects
common websites adresses to the local IP adress.

NOTE: It is necessary to clear cache so that browsers
sessions are cleared.
"""

import os
import colorama
from colorama import Fore, Back
import sys
import re

colorama.init()

# COLORS
Y, R = Fore.YELLOW, Fore.RED

BB, BBL, YY = Back.BLUE, Back.BLACK, Back.YELLOW

# TODO: 

# Define the ASCII art
ascii_art = """\n\n\n
#==============================================|
# /\_/\  Looks like you found out that I'm     |
#( o.o ) blocking your sites hehe.             |
# > ^ <  - kenken                              |
#/  ~  \\                                       |
#==============================================|
\n\n\n
"""

ascii_art2 = """\n\n\n
#=================================================
#  ,_     _
# |\\_,-~/
# / _  _ |    ,--.     Spare me for I have sinned!
#(  @  @ )   / ,-'      - kenken
# \  _T_/-._( (
# /         `.  ~-.
#|         _  `~'-.
# \ \ ,  /      ~-.`-.
#  || |-_\           ~-.
# ((_/`(__________,-'
#=================================================
"""

ascii_art3 ="""\n
  / \__                                     This tool blocks access from
 (    @\____                                common websites and retrieve 
 /         O   DNS PRANKER.                 bookmarks from the target PC 
/   (_____/    - kenken                     and blocks all websites from 
/_____/   U                                 those booksmarks. \n
"""


# Check the current OS, since every OS have different hosts 
# file destination.
if os.name == 'nt':
    dest = "c:\Windows\System32\Drivers\etc\hosts" 

else: 
    dest = "/etc/hosts"

User = os.getenv('USERNAME')
# List of bookmarks directory from different browsers and OS.
bookmarks_dir = [
         f"C:/Users/{User}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks",
         f"C:/Users/{User}/AppData/Roaming/Opera Software/Opera GX Stable/Bookmarks",
         f"C:/Users/{User}/AppData/Roaming/Opera Software/Opera Stable/Bookmarks",
         ]


# List of sites to block.
sites = ["youtube.com", "facebook.com", "messenger.com", "google.com"]


def getBooksmarksFile(bookmarks_dir) -> list:
    with open(bookmarks_dir, 'r') as f:
        file = f.read()
    return file

def getUrl(file: str) -> list:
    bookmarks = re.findall(r'"url":.*', file)
    for i in range(len(bookmarks)):
        bookmarks[i] = bookmarks[i].removeprefix('"url": ').strip('"')
    return bookmarks


def flushDNS() -> None:
    print(f"[*]{BB}INFO{BB}:{BBL}{Y} Flushing DNS...")
    os.system("ipconfig/flushdns")
    print(f"[*]{BB}INFO:{BBL}{Y} DNS successfully flushed.")

def clearTemp() -> None:
    print(f"[*]{BB}INFO:{BBL}{Y} Deleting TEMP files...")
    files_num = len(os.listdir())
    os.system("del /q /f %temp%\\")
    deleted_files = files_num - len(os.listdir())
    print(f"[*]{BB}INFO:{BBL}{Y} Deleted {deleted_files} TEMP files.")

def changeHosts(sites: list) -> None:
    print(f"{BBL}{Y}[*]{BB}INFO:{BBL}{Y} Changing hosts file...")
    print(f"[*]{BB}INFO:{BBL}{Y} Blocking sites...")
    with open(dest, 'a') as f:
        f.write(ascii_art)
 
    with open(dest, 'a') as f:
        f.write("# You can delete the blocked sites now lol \(o _ o)/\n\n")

    for site in sites:
        with open(dest, 'a') as f:
            f.write(f"0.0.0.0    {site}\n")
            print(f"[*]{BB}INFO:{BBL}{Y} www.{site} blocked.")
    with open(dest, 'a') as f:
        f.write(ascii_art2)
    print(f"[*]{BB}INFO:{BBL}{Y} All sites have been blocked.")

def main():
    print("=" * 100)
    print(ascii_art3)
    print("=" * 100)
    print('\n\n')
    print(f"{Y}[*]{BB}INFO:{BBL}{Y} Finding bookmarks...")
    for bookmarks in bookmarks_dir:
        Booksmarks = []
        try:
            Booksmarks = getUrl(getBooksmarksFile(bookmarks))
        except FileNotFoundError:
            print(f"[*]{YY}{R}WARNING:{BBL} {Y}No bookmarks for {bookmarks}, continuing...")

        Booksmarksnum = len(Booksmarks)
        print(f"[*]{BB}INFO:{BBL}{Y} Found {Booksmarksnum}.")
        print(f"[*]{BB}INFO:{BBL}{Y} Adding the found bookmarks to the list to block...")
        sites.extend(Booksmarks)

    try:
        #flushDNS()
        #clearTemp()
        pass
    except:
        print(f"[*]{BB}INFO:{BBL}{Y} Cannot flush caches.")
        print(f"[*]{BB}INFO:{BBL}{Y} Continuing...")

    try:
       changeHosts(sites)
    except PermissionError:
        print(f"[*]{BB}INFO:{BBL}{Y} You must run the script as admin.")
    input()
    print(f"[*]{BB}INFO:{BBL}{Y} Exiting...")

if __name__ == "__main__":
    main()


