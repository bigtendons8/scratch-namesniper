import requests

link = 'https://api.scratch.mit.edu/accounts/checkusername/'
count = 0
free = []

with open("list", "r") as file:
    words = file.read().split("\n")

def writefree():
    with open('output', 'w') as file:
        file.writelines(free)


try:
    for word in words:
        s = requests.Session()
        r = s.get(link+word)
        if r.json()['msg'] == 'valid username':
            print(word + ": free")
            free.append(word + '\n')
            count += 1
            print(str(count) + '/' + str(len(words)) + 'complete. ' + str(len(free)) + ' names found.')
        else:
            count += 1
            print(str(count) + '/' + str(len(words)) + 'complete. ' + str(len(free)) + ' names found.')
except KeyboardInterrupt:
    writefree()
    raise SystemExit

writefree()
