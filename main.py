
import requests


def main():
    with open("list.txt", "r") as file:
        words = file.read().strip().split("\n")


    def writefree():
        with open('output.txt', 'w') as file:
            file.writelines(free)


    LINK = 'https://api.scratch.mit.edu/accounts/checkusername/'
    free = []
    s = requests.Session()

    try:
        for count, word in enumerate(words):
            r = s.get(LINK + word)
            if r.json()['msg'] == 'valid username':
                print(f"{word}: available")
                free.append(f"{word}\n")
            else:
                print(f"{word}: unavailable")
            print(f"{count+1}/{len(words)} complete. {len(free)} names found. ({round((count+1)/len(words)*100)}%)")
    except KeyboardInterrupt:
        writefree()
        raise SystemExit

    writefree()


if __name__ == "__main__":
    main()
