
import requests

with open("list.txt", "r") as file:
    words = file.read().strip().split("\n")


def main():
    def writefree():
        with open('output.txt', 'w') as file:
            file.writelines(free)

    link = 'https://api.scratch.mit.edu/accounts/checkusername/'
    free = []
    s = requests.Session()

    try:
        for count, word in enumerate(words):
            r = s.get(link + word)
            if r.json()['msg'] == 'valid username':
                print(f"{word}: available")
                free.append(f"{word}\n")
            else:
                print(f"{word}: unavailable")
            print(f"{count+1}/{len(words)} complete. {len(free)} names found.")
    except KeyboardInterrupt:
        writefree()
        raise SystemExit

    writefree()


if __name__ == "__main__":
    main()
