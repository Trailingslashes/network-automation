# Aruba CX Collection

## Install Aruba galaxy collection
`ansible-galaxy collection install arubanetworks.aoscx`

## Prepare switches for Ansible
```
ssh server vrf mgmt
https-server rest access-mode read-write
https-server vrf mgmt
# if using OOBM
# oobm; ip address $IP
```

