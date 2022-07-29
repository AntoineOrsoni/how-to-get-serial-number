from genie.testbed import load

testbed = load('./testbed.yaml')
iosxr = testbed.devices["R1"]

# Connect to the device
iosxr.connect(init_exec_commands=[], 
            init_config_commands=[], 
            log_stdout=False,
            learn_hostname=True)

# Collecting the structured output
show_inventory = iosxr.parse('show inventory')

print(show_inventory)

# Disconnect from the device
iosxr.disconnect()