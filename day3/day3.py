from util.get_content import get_content


def main():
    filename = "day3.txt"
    content = get_content(filename)
    content = content.splitlines()

    # Part 1

    counter = 0
    # for rucksack in content:
    #     counter += get_amt(rucksack)
    for i in range(0, len(content) - 2, 3):
        rucksacks = [content[i], content[i + 1], content[i + 2]]
        counter += get_triplet(rucksacks)

    print(counter)


def get_triplet(rucksack: list[str]):
    letterlist = []
    counter = 0
    for letter in rucksack[0]:
        if letter in rucksack[1] and letter in rucksack[2] and letter not in letterlist:
            letterlist.append(letter)
            if letter.upper() == letter:
                counter += ord(letter) - 38
            elif letter.lower() == letter:
                counter += ord(letter) - 96
    return counter


def get_amt(rucksack: str):
    first_part = rucksack[: len(rucksack) // 2]
    second_part = rucksack[len(rucksack) // 2 :]
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
