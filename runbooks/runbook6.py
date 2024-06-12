import warnings

from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

warnings.filterwarnings("ignore")

nr = InitNornir(config_file="config.yml")


def send_configs_test(task):
    if task.host.platform == "aruba_aoscx":
        task.run(
            task=send_configs,
            configs=[
                "router ospf 44",
                "router-id 4.4.4.4",
                "area 0.0.0.44",
            ],
        )
    elif task.host.platform == "arista_eos":
        task.run(
            task=send_configs,
            configs=["router ospf 44", "network 0.0.0.0 255.255.255.255 area 44"],
        )


results = nr.run(task=send_configs_test)

print_result(results)
