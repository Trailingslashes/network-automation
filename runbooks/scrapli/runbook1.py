from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Load the nornir yml config file
nr = InitNornir(config_file="config.yml")

results = nr.run(task=send_command, command="show version")

print_result(results)
