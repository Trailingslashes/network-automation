from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

command_list = ["show ip int br", "show version", "show run"]


def show_command_test(task):
    task.run(task=send_commands, commands=command_list, strip_prompt=True)


results = nr.run(task=show_command_test)

print_result(results)
