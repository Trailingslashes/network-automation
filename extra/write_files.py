with open('myfile.txt', 'a') as f: # append
  f.write('Just a line\n')
  f.write('Just a second line')
  f.close()
  
with open('myfile.txt', 'r+') as f:
  f.seek(5)
  f.write('100')
  f.write('Line edit with our r+\n')