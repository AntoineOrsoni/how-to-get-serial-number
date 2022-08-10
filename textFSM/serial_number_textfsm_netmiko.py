import textfsm
from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

ssh = ConnectHandler(**cisco_router)
output = ssh.send_command('show inventory all')
ssh.disconnect()

with open('./serial_number.template') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)

for entry in result:
    if 'Rack 0' in entry: serial_number = entry[2]
print(f'My device serial number is: {serial_number}')