from netmiko import ConnectHandler
from inventory import routers

USERNAME = "vyos"
PASSWORD = "vyos"

for router in routers:

    device = {
        "device_type": "vyos",
        "host": router["host"],
        "username": USERNAME,
        "password": PASSWORD,
    }
    print(f"Connecting to {router['name']}")
    print(device)
    connection = ConnectHandler(**device)

    output = connection.send_command(
        "show configuration commands",
        expect_string=r"[@~#$]"
    )
    filename = f"../configs/{router['name']}.txt"

    with open(filename,
              "w") as file:
        file.write(output)

    connection.disconnect()

    print(f"SUCCESS: {router['name']}")
print("Backup Complete")
