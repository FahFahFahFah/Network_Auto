#Second Step: Enum
#gobuster in directory enumeration mode

import subprocess
import re
import os

def run_gobuster(ip_addr):
    url = 'http://' + str(ip_addr)
    wordlist = '/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt'
    gobuster_command = ["gobuster", "dir", "-u", url, "-w", wordlist]
    
    file_name = 'gobusterresult' + (ip_addr) + '.txt'
    if os.path.exists(file_name):
        os.remove(file_name)

    with open(file_name, 'w') as file:
        subprocess.run(gobuster_command, stdout=file)

    urls = []
    with open(file_name, 'r') as file:
        for line in file:
            match = re.search(r'\[-->\s*(https?://\S+)\]', line)
            if match:
                url = match.group(1)
                urls.append(url)

    return urls
    