from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

# Load the nornir yml config file
nr = InitNornir(config_file="config.yml")


def ntp_config(task):
    task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")


results = nr.run(task=ntp_config)
print_result(results)
