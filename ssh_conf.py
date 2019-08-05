import paramiko
import time
import getpass

ip_address = input('Enter ip address : ')
username = input('Enter username : ')
password = getpass.getpass('Password : ')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print(f'sucess login to {ip_address} ..')
print('1. Setting IP Address')
print('2. Backup Config')
pil = input('What you want ? (1-2) : ')
conn = ssh_client.invoke_shell()

if pil==1 :

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 192.168.10.0 255.255.255.0\n")
    time.sleep(1)

    output = conn.recv(65535)
    print output
    ssh_client.close()

elif pil==2 :
    conn.send("terminal length 0\n")
    conn.send("show run\n")
    time.sleep(1)
    output = conn.recv(65535)
    output_file=open(f"{ip_address}.cfg","w")
    output_file.write(output)
    output_file.close()
    print(f"Config in {ip_address} saved !!")
    ssh_client.close()










