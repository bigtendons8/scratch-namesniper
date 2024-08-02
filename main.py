import requests
<<<<<<< HEAD

link = 'https://api.scratch.mit.edu/accounts/checkusername/'
count = 0
free = []
s = requests.Session()

with open("list", "r") as file:
    words = file.read().split("\n")

def writefree():
    with open('output', 'w') as file:
        file.writelines(free)
=======
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
>>>>>>> origin/main


try:
    for word in words:
<<<<<<< HEAD
        r = s.get(link+word)
        if r.json()['msg'] == 'valid username':
            print(f"{word}: available")
            free.append(f"{word}\n")
        else:
            print(f"{word}: unavailable")
        count += 1
        print(f"{count}/{len(words)} complete. {len(free)} names found.")
=======
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
>>>>>>> origin/main
except KeyboardInterrupt:
    writefree()
    raise SystemExit

<<<<<<< HEAD
writefree()
=======
writefree()
>>>>>>> origin/main
