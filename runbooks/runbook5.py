import warnings

from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

warnings.filterwarnings("ignore")

nr = InitNornir(config_file="config.yml")


def send_config_test(task):
    task.run(task=send_config, config="ntp server 55.66.11.33")


results = nr.run(task=send_config_test)

print_result(results)
