import paramiko

pm = paramiko.SSHClient()

def Menu():
	print("#------------- Pilih Node -------------#")
	print("1. Node 1 [IP: " + node1_ip + "]")
	print("2. Node 2 [IP: " + node2_ip + "]")
	print()
	node = int(input("Pilih Node: "))
	return node

def connect(ip, name, pw):
	pm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	pm.connect(hostname=ip, username=name, password=pw)

node1_ip = "192.168.0.66"
node1_name = "hooman"
node1_pw = "hooman"

node2_ip = "192.168.0.67"
node2_name = "hooman"
node2_pw = "hooman"

node = Menu()
if(node == 1):
	connect(node1_ip, node1_name, node1_pw)
elif(node == 2):
	connect(node2_ip, node2_name, node2_pw)
else:
	print("Silahkan coba lagi")
	exit()

while(True):
    stdin,stdout,stderr = pm.exec_command("python3 CPU,Memory,TxRx.py")
    output = stdout.readlines()
    for i in output:
        print(i, end="")