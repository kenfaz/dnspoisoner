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

colorama.init()

# COLORS
Y = Fore.YELLOW

BB, BBL = Back.BLUE, Back.BLACK

# TODO: Create a function to get all bookmarks in the local machine.
# TODO: Create a function to get all urls from the complicated structure of the json file.
# TODO: Add those sites to the list of sites.


# Add more sites.

# Define the ASCII art
ascii_art = """\n\n\n
#==============================================|
# /\_/\  Looks like you found out!             |
#( o.o ) Btw I'm a cat that pranks people hehe.|
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



# Check the current OS, since every OS have different hosts 
# file destination.
if os.name == 'nt':
    dest = "c:\Windows\System32\Drivers\etc\hosts" 

else: 
    dest = "/etc/hosts"

# List of sites to block.
sites = ["youtube.com", "facebook.com", "messenger.com"]



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


