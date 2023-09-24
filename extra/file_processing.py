nested_list = []

with open('devices.txt') as f:
    lines = f.readlines()

for line in lines[1:]:
    # Remove trailing newlines and split the line based on a colon
    nested_list.append(line.strip().split(':'))


print(nested_list)

# ping each device from the nested list
for devices in nested_list:
    print(f'pinging {devices[1]}')
