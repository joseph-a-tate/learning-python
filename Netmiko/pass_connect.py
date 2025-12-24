from netmiko import ConnectHandler

net_connect = ConnectHandler(
        device_type="cisco_ios",
        host="192.168.0.1",
        username="username",
        password="password"
    )

#netconnect should be a usable SSH connection to the remote device
"""
net_connect.find_prompt()
    #prints "ciscoX#"

output = net_connect.send_command("sho ip arp")
print(output)
    #prints sho ip arp

cfg_list = [
        "ip access-list extended EXAMPLE",
        "permit ip any host 1.1.1.1",
        "permit ip any host 1.1.1.2",
        "permit ip any host 1.1.1.3",
        "permit ip any host 1.1.1.4",
        "permit ip any host 1.1.1.5"
    ]

output = net_connect.send_config_set(cfg_list)
print(cfg_output)

net_connect.save_config()
    #performs a 'copy running-config startup-config' command

"""
