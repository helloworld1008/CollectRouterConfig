# CollectRouterConfig

CollectRouerConfig is a python-based utility for Linux machines that:

- Takes configuration backups of Juniper (JUNOS) routers.
- Creates an SSH connection to each router, runs the "show configuration" command and collects the output in a separate file for each router
- Displays the reason for error if the script fails to establish an SSH connection with the router
