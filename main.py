import requests
#import random

link = 'https://api.scratch.mit.edu/accounts/checkusername/'
count = 0

file = open("list", "r")
data = file.read()
words = data.split("\n")
file.close()

#OR

#words = []

free = []

#random.shuffle(words)

def writefree():
    file = open('output', 'a')
    file = open('output', 'w')
    file.writelines(free)
    file.close()


try:
    for word in words:
        s = requests.Session()
        r = s.get(link+word)
        if r.json()['msg'] == 'valid username':
            print(word + ": free")
            free.append(word + '\n')
            count += 1
            print(str(count)+'/'+str(len(words))+'complete. '+str(len(free))+'names found.')
        else:
            count += 1
            print(str(count) + '/' + str(len(words)) + 'complete. ' + str(len(free)) + ' names found.')
except KeyboardInterrupt:
    writefree()
    raise SystemExit

writefree()