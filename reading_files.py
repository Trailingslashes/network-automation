# f = open('config.txt', 'rt') # 't' - text file

# content = f.read()
# print(content)
# f.close()
# print(f.closed)

# return as a list
with open('config.txt') as file:
  content = file.read().splitlines()
  print(content)
print(file.closed)

print("#" * 50)


with open('config.txt') as f:
  print(f.readline(), end='')
  print(f.readlines())
print(file.closed)

print("#" * 50)

with open('config.txt') as f:
  content = list(f)
  print(content)
  print(type(content))
  
with open('config.txt') as f:
  for line in f:
    print(line, end='\n')