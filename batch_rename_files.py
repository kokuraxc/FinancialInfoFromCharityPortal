import os

for f in os.listdir('test/'):
    print(f)
    os.rename('test/' + f, 'test/' + f[:-4] + '_m' + f[-4:])
