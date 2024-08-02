
import requests

with open("list.txt", "r") as file:
    words = file.read().strip().split("\n")


def writefree():
    with open('output.txt', 'w') as file:
        file.writelines(free)


def main():
    link = 'https://api.scratch.mit.edu/accounts/checkusername/'
    count = 0
    free = []
    s = requests.Session()

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


if __name__ == "__main__":
    main()
