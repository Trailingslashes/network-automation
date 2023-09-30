# network-automation


## Install Ansible on Ubuntu
`sudo apt -y install software-properties-common`
`sudo add-apt-repository --yes --update ppa:ansible/ansible`
`apt -y install ansible`

## Install Ansible via Virtualenv
`sudo apt-get install python3-virtualenv`
`sudo apt-get install python3-pip`
`python3 -m virtualenv ~/ansible`
`source ~/ansible/bin/activate`
`pip3 install ansible`
