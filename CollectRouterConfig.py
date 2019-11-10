#!/usr/bin/env python

import paramiko, time, sys
from paramiko.ssh_exception import *
import socket


### Credentials ###

uname = 'admin'
pwd = 'admin1'



### Function definition ###

def est_sess_run_cmd(IP, username, password):

        clnt = paramiko.client.SSHClient()

        clnt.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

        clnt.connect(IP, username=username, password=password)

        time.sleep(1)


        ch = clnt.invoke_shell()

        time.sleep(1)

        backup_file_name = IP.rstrip() + "_config"

        backup_file_object = open(backup_file_name, 'w')

        orig_stdout = sys.stdout

        sys.stdout = backup_file_object

        ch.send("show configuration | display-set | no-more\n")

        time.sleep(1)

        while ch.recv_ready():

                print "\b" + ch.recv(1000),
                time.sleep(0.5)

        ch.send("exit\n")

        ch.close()

        clnt.close()

        backup_file_object.close()

        sys.stdout = orig_stdout



### Main program starts here ###

if __name__ == '__main__':

        try:

                ip_file_object = open('IP_file', 'r')

        except IOError as e:

                if e.args[1] == 'No such file or directory':

                        print "\nIP_file not found...Exiting\n"

                        sys.exit(0)

        else:

                print ""

                for ip in ip_file_object:

                        print "Initiating backup for {0}".format(ip)

                        try:
                                est_sess_run_cmd(ip, uname, pwd)

                        except (AuthenticationException, BadAuthenticationType, BadHostKeyException, ChannelException, NoValidConnectionsError, PartialAuthentication, PasswordRequiredException, ProxyCommandFailure, SSHException, socket.gaierror) as e:

                                print e
                                print "" 

                        else:

                                print "Backup completed\n"

                ip_file_object.close()
