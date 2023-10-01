# Aruba CX Collection

## Install Aruba galaxy collection
`ansible-galaxy collection install arubanetworks.aoscx`
`ansible-galaxy install arubanetworks.aoscx_role`
`apt-get install curl openssl libcurl4-openssl-dev libssl-dev python3-dev` # required for Ubuntu

## Prepare switches for Ansible
```
ssh server vrf mgmt
https-server rest access-mode read-write
https-server vrf mgmt
# if using OOBM
# oobm; ip address $IP
```

