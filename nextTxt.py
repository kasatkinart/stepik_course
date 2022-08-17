import requests
adr = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt', 'r') as inputFile:
    s = inputFile.readline().strip()
    r = requests.get(s)

while 'We' not in r.text:
    s = adr + r.text
    r = requests.get(s)
    print(r.text)

print(s)


