from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")


def show_command_test(task):
    task.run(task=send_commands_from_file, file="configs/show_version.txt")


results = nr.run(task=show_command_test)
print_result(results)
