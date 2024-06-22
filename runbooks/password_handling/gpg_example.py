#  pip install python-gnupg
#  gpg --gen-key , follow prompts
# create a folder with a txt file with the following variables
# DEFAULT_USERNAME=
# DEFAULT_PASSWORD=
# gpg --symmetric -o enc.env.gpg passwords
# gpg --decrypt enc.env.gpg
# flush gpg cache
# echo RELOADAGENT | gpg-connect-agent

# gpg --decrypt passwords.gpg > passwords_decrypted
# echo "NEW_LINE=new_value" >> passwords_decrypted
# gpg --symmetric --cipher-algo AES256 --output passwords_new.gpg passwords_decrypted
# mv passwords_new.gpg passwords.gpg
# shred -u passwords_decrypted
# echo RELOADAGENT | gpg-connect-agent
import os

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")


nr.inventory.defaults.username = os.environ["DEFAULT_USERNAME"]
nr.inventory.defaults.password = os.environ["DEFAULT_PASSWORD"]


def cred_test(task):
    task.run(send_command, command="show version")


results = nr.run(task=cred_test)

print_result(results)
