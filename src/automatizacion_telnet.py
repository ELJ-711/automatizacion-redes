
import getpass
import telnetlib

HOST = "192.168.185.70"
user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username:", timeout=10)
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password:", timeout=10)
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
enable_password = getpass.getpass("Enable password: ")
tn.write(enable_password.encode("ascii") + b"\n")
tn.write(b"configure terminal\n")

tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 2.2.2.2 0.0.0.0 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
