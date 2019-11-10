# CollectRouterConfig

CollectRouerConfig is a python-based utility for Linux machines that:

- Takes configuration backups of Juniper (JUNOS) routers.
- Creates an SSH connection to each router, runs the "show configuration" command and collects the output in a separate file for each router
- Displays the reason for error if the script fails to establish an SSH connection with the router

## Prerequisites

This script requires paramiko python library to be installed

## Usage

- Create a file named "IP_file" containing the IP address of routers you are working on. The file must be in the same directory where the script is located

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

- Give executable permissions to your script
```bash
$ chmod 755 CollectRouerConfig.py
$
```

- Run the script
```
$ ./CollectRouterConfig.py 

Initiating backup for 192.9.200.101

Backup completed

Initiating backup for a.b.c.d

[Errno -2] Name or service not known

Initiating backup for 192.9.200.106

Backup completed

$
```

- The configuration files of each router will be generated in the same folder
```
$ ls
192.9.200.101_config  192.9.200.106_config  CollectRouterConfig.py  IP_file
$ 
```

- cat the config files to display the router configuration
```
$ cat 192.9.200.101_config | more
Last login: Sun Jul 12 18:06:28 2019 from 192.168.100.130

admin@Router_1> show configuration | display-set | no-more 
set system ne-id 101
set system host-name Router_1
set system login user admin class super-user
set system login user admin full-name Administrator
set system login user admin uid 1001
set system syslog file user.log user any
set system pm-options pm-monitor-start-time 2019-11-05,15:28:05
set system pm-options pm-monitor-end-time 2020-04-17,15:28:07
set interfaces ce-ts2/1 unit 0 family inet address 10.10.13.1/255.255.255.252
set interfaces ce-ts2/1 unit 0 family mpls
set interfaces ce-ts2/1 unit 0 family iso
set interfaces ce-ts7/1 unit 0 family inet address 10.10.12.1/255.255.255.252
set interfaces ce-ts7/1 unit 0 family mpls
set interfaces ce-ts7/1 unit 0 family iso
set interfaces xe-xsa/1 unit 0 family inet address 10.10.110.2/255.255.255.252
set interfaces lo0 unit 0 family inet address 100.100.100.100/255.255.255.255
set interfaces lo0 unit 0 family iso
set protocols bfd interface ce-ts2/1.0 destination 10.10.13.2 minimum-receive-interval 3.33
set protocols bfd interface ce-ts2/1.0 destination 10.10.13.2 minimum-transmit-interval 3.33
set protocols bfd interface ce-ts2/1.0 destination 10.10.13.2 multiplier 3
set protocols bfd interface ce-ts7/1.0 destination 10.10.12.2 minimum-receive-interval 3.33
set protocols bfd interface ce-ts7/1.0 destination 10.10.12.2 minimum-transmit-interval 3.33
set protocols bfd interface ce-ts7/1.0 destination 10.10.12.2 multiplier 3
set protocols bfd minimum-receive-interval 3.33
set protocols bfd minimum-transmit-interval 3.33
set protocols bfd multiplier 3
set protocols isis protocol-instance 1 enable
set protocols isis protocol-instance 1 level 2 wide-metrics-only enable
set protocols isis protocol-instance 1 interface ce-ts2/1.0 emulate-ptp
set protocols isis protocol-instance 1 interface ce-ts2/1.0 level-type L2
set protocols isis protocol-instance 1 interface ce-ts2/1.0 bfd
set protocols isis protocol-instance 1 interface ce-ts7/1.0 emulate-ptp
set protocols isis protocol-instance 1 interface ce-ts7/1.0 level-type L2
set protocols isis protocol-instance 1 interface ce-ts7/1.0 bfd
set protocols isis protocol-instance 1 interface lo0.0 passive
set protocols isis protocol-instance 1 interface lo0.0 level-type L2
set protocols isis protocol-instance 1 iso-addressing area-address 49.0001
set protocols isis protocol-instance 1 iso-addressing system-id 0010.0100.1001
set protocols isis protocol-instance 1 fast-reroute-options enable
set protocols isis protocol-instance 1 fast-reroute-options remote-lfa
set protocols isis protocol-instance 1 level-type L2
set protocols ldp enable
set protocols ldp fast-reroute enable
set protocols ldp fast-reroute remote-lfa-enable
$
```
