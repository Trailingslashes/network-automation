# napalm example
# aruba-cx require pyaoscx version 1.0.0
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

# Initialize Nornir with the configuration file
nr = InitNornir(config_file="config.yml")

# Function to ping a specific IP address using napalm
def ping(task):
    # Ping the IP address 192.168.150.137 on each device
    task.run(task=napalm_ping, dest="192.168.150.133")

# Execute the ping f
# unction across devices and store results
results = nr.run(task=ping)

# Print the results of the ping
print_result(results)
