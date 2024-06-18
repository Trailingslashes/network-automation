from nornir import InitNornir
from nornir_scrapli.tasks import send_command  # send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")


def show_command_test(task):
    if task.host.platform == "aruba_aoscx":
        task.run(
            send_command,
            command=f"copy running-config tftp://192.168.150.130/{task.host}.cfg cli vrf mgmt",
        )
    elif task.host.platform == "eos":
        task.run(
            send_command,
            command=f"copy running-config tftp://192.168.150.130/{task.host}.cfg",
        )


results = nr.run(task=show_command_test)
print_result(results)
