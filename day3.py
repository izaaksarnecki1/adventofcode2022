from get_content import get_content

def main():
    filename = 'day3.txt'
    content = get_content(filename)
    content = content.splitlines()

    # Part 1

    counter = 0
    for rucksack in content:
        counter += get_amt(rucksack)
    print(counter)


def get_amt(rucksack):
    first_part = rucksack[:len(rucksack)//2]
    second_part = rucksack[len(rucksack)//2:]
    letterlist = []
    counter = 0
    for letter in first_part:
        if letter in second_part and letter not in letterlist:
            letterlist.append(letter)
            if letter.upper() == letter:
                counter += ord(letter) - 38
            elif letter.lower() == letter:
                counter += ord(letter) - 96
    return counter

main()
