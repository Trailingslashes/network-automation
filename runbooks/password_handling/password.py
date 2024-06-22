import getpass

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")
password = getpass.getpass("Enter password: ")
nr.inventory.defaults.password = password


def credential_test(task):
    task.run(send_command, command="show version")


nr.run(credential_test)
print_result(nr)
