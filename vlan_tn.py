import telnetlib
import getpass

host = input("Enter Device IP Address : " )
user = input("Enter your Telnet username : ")
vlan = int(input("Total VLAN'S : "))
password = getpass.getpass();

tn = telnetlib.Telnet(host)

devices = host.split()

for x in devices :
    print("Configuring "+(x)+"...")
    tn.read_until("Username: ")
    tn.write(user + "\n" )
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n" )

    tn.write("conf t\n")
    for x in range (1,vlan+1):
        tn.write("vlan + str(x) + "\n" )
        tn.write("name vlan" + str(x) + "\n")

    tn.write("end\n")
    tn.write("exit\n")
    print("Done ...")


print tn.read_all()
