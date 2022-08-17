with open('dataset_3378_2.txt', 'r') as inputFile:
    s = inputFile.readline().strip()

print(s)

import requests
r = requests.get(s)
print(len(r.text.splitlines()))