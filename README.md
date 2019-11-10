# CollectRouterConfig

CollectRouerConfig is a python-based utility for Linux machines that:

- Takes configuration backups of Juniper (JUNOS) routers.
- Creates an SSH connection to each router, runs the "show configuration" command and collects the output in a separate file for each router
- Displays the reason for error if the script fails to establish an SSH connection with the router

## Prerequisites

This script requires paramiko python library to be installed

## Usage

- Create a file named "IP_file" containing the IP address of routers you are working on. The file must be in the same directory where the script is located
- Run the script

```bash
$ cat IP_file 
192.168.200.101
a.b.c.d
192.168.200.106
$  
$ ls 
CollectRouterConfig.py  IP_file
$ 
```

