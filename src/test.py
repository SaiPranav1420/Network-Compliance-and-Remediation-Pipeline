from netmiko import ConnectHandler

device = {
    "device_type": "vyos",
    "host": "192.168.56.11",
    "username": "vyos",
    "password": "vyos"
}

conn = ConnectHandler(**device)

print(conn.send_command("show version"))

conn.disconnect()
