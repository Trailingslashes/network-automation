nested_list = []

with open('devices.txt') as f:
	lines = f.readlines()

for line in lines[1:]:
    # Remove trailing newlines and split the line based on comma
    nested_list.append(line.strip().split(','))

print(nested_list)

f.close()