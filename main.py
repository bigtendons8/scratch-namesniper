
import requests

link = 'https://api.scratch.mit.edu/accounts/checkusername/'
count = 0
free = []
s = requests.Session()

with open("list", "r") as file:
    words = file.read().split("\n")

def writefree():
    with open('output', 'w') as file:
        file.writelines(free)

try:
    for word in words:
        r = s.get(link + word)
        if r.json()['msg'] == 'valid username':
            print(f"{word}: available")
            free.append(f"{word}\n")
        else:
            print(f"{word}: unavailable")
        count += 1
        print(f"{count}/{len(words)} complete. {len(free)} names found.")
except KeyboardInterrupt:
    writefree()
    raise SystemExit

writefree()
