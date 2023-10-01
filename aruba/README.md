# Aruba CX Collection

## Prepare switches for Ansible
```
interface mgmt
no shutdown
ip dhcp # or static
```

Config an admin user for ansible to use:
`user admin group administrators password plaintext mypassword`

In the config menu:
```
ssh server vrf mgmt
ssh server vrf default
https-server vrf mgmt
https-server vrf default
https-server rest access-mode read-write
```

## Install Aruba galaxy collection
`ansible-galaxy collection install arubanetworks.aoscx`
`ansible-galaxy install arubanetworks.aoscx_role`
`apt-get install curl openssl libcurl4-openssl-dev libssl-dev python3-dev` # required for Ubuntu