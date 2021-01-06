# Server_shell.py
Server shell by python 
There are many ways to gain control over a compromised system, a common way is to gain interactive shell access,
which enables you to try to gain full control of the operating system. However, most basic firewalls blocks direct remote connections.
One of the methods to bypass this, is to use reverse shells.
A reverse shell is a program that executes local cmd.exe (for Windows) or bash/zsh (for Unix-Like) commands and sends the output to a
remote machine. With a reverse shell, the target machine initiates the connection to the attacker machine, and the attacker’s machine listens
for incoming connections on a specified port,
this will bypass firewalls.
