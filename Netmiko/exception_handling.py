from netmiko import ConnectHandler
from netmiko.exceptions import SSHException, NetMikoTimeoutException, NetMikoAuthenticationException

# list 0 is the correct and list index 1 is incorrect
values = [["cisco_ios", "192.168.0.1", "username", "password"],
          ["cicso_ios", "192.168.0.1.1", "ussername", "passw0rd"]]

"""
net_connect = ConnectHandler(device_type=Good[0],host=Good[1],username=Good[2],password=Good[3])
#completes successfully
"""

for x in range(4):
    try:
        #finds the value to be wrong and sets it to one in the offset
        offset = [0,0,0,0]
        offset[x] = 1

        #creates the device paramaters for ConnectHandler
        device = {"device_type":values[offset[0]][0],
                "host":values[offset[1]][1],
                "username":values[offset[2]][2],
                "password":values[offset[3]][3]
            }

        # creates the connect handler and trips the exception
        net_connect = ConnectHandler(**device)

    except NetMikoTimeoutException:
        print("Connection timed out, trying again...")
    except SSHException:
        print("Error with SSH Exception, verify certificates on machine.")
    except NetMikoAuthenticationException:
        print("Authentication failed, please check credentials.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

