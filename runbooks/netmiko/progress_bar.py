import os

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from tqdm import tqdm

nr = InitNornir(config_file="config.yml")

# Set the defaults from env gpg
nr.inventory.defaults.username = os.environ["DEFAULT_USERNAME"]
nr.inventory.defaults.password = os.environ["DEFAULT_PASSWORD"]


def send_command(task, progress_bar):
    task.run(task=netmiko_send_command, command_string="show version")
    progress_bar.update()


with tqdm(total=len(nr.inventory.hosts)) as progress_bar:
    results = nr.run(task=send_command, progress_bar=progress_bar)
print_result(results)
