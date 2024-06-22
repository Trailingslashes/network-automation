# TEXTFSM TEMPLATES
# Order of preference is:
# 1) Find directory in `NET_TEXTFSM` Environment Variable.
# 2) Check for pip installed `ntc-templates` location in this environment.
# 3) ~/ntc-templates/ntc_templates/templates.
# ipdb.set_trace()

import os

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

# Set the defaults from env gpg
nr.inventory.defaults.username = os.environ["DEFAULT_USERNAME"]
nr.inventory.defaults.password = os.environ["DEFAULT_PASSWORD"]
# Set the NET_TEXTFSM environment variable from the defaults
os.environ["NET_TEXTFSM"] = "path to textfsm templates"


def test_this(task):
    print(f"Host {task.host.name} platform: {task.host.platform}")
    show_interface = task.run(
        task=netmiko_send_command, command_string="show interface", use_textfsm=True
    )

    print(f"Raw result type: {type(show_interface.result)}")

    # Print the parsed data
    if isinstance(show_interface.result, list):
        print(f"Number of interfaces parsed: {len(show_interface.result)}")
        for interface in show_interface.result:
            print(f"Interface: {interface.get('interface', 'N/A')}")
            print(f"Status: {interface.get('status', 'N/A')}")
            print(f"Description: {interface.get('description', 'N/A')}")
            print("---")
    else:
        print("TextFSM parsing did not return a list as expected.")


results = nr.run(task=test_this)
print_result(results)
