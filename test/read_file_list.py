import os

files = os.listdir('%s/images/47475' % os.getcwd())

for file in files:
    print(os.path.join('%s/images/47475' % os.getcwd(), file))